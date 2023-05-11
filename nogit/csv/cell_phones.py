import boto3
from botocore.client import Config
from csv import reader, writer
from pprint import pprint

from sqlalchemy.sql.functions import user
from queries import get_np_id_by_email

def get_client(service: str, region = 'us-west-2'):
    return boto3.client(
        service, region_name=region, config=Config(signature_version="s3v4")
    )
def get_cognito_client():
    return get_client("cognito-idp")


def get_sso_user_by_email(email: str) -> dict:
    return get_cognito_client().admin_get_user(UserPoolId='us-west-2_VODHRFn7A', Username=email)

with open('get_lada.csv') as csv_file, open('./cellphones.csv', 'w') as outFile:
    csv_reader = reader(csv_file, delimiter=',')
    write = writer(outFile, delimiter=',')
    attrs = {}
    line_count = -1
    row_to_write = []
    for row in csv_reader:
        line_count +=1
        if line_count != 0:
            sso_id =row[0]
            try:
                response = get_sso_user_by_email(sso_id)
                user_data = response.get("UserAttributes") or []
            except:
                user_data = ""
            if not user_data:
                row_to_write.append(sso_id)
                row_to_write.append("ESTE USUARIO NO EXISTE")
                write.writerow(row_to_write)
            else:
                for attr in user_data:
                    attrs[attr["Name"]] = attr["Value"]
                try:
                    print(attrs['email'])
                    person = get_np_id_by_email(attrs['email'])
                except:
                    person = None
                if person:
                    primary_phone = next((p for p in person.phones if p.is_primary == 1), None,)
                    row_to_write.append(sso_id)
                    row_to_write.append(attrs['email'])
                    MESSAGE = f"NO TIENE TELEFONO PRIMARIO WTF {primary_phone}"
                    if primary_phone:
                        pprint(f"{line_count} email:{attrs['email']} id: {person.id} telefono: {primary_phone.number} estatus: {primary_phone.status_id}")
                        row_to_write.append(primary_phone.country_code+primary_phone.number)
                        row_to_write.append(primary_phone.status_id)
                        row_to_write.append(row[2])
                        MESSAGE = " NO VERIFICADO"
                        if primary_phone.status_id == 21:
                            MESSAGE = "VERIFICADO"
                    row_to_write.append(MESSAGE)
                    write.writerow(row_to_write)
                else:
                    row_to_write.append(sso_id)
                    row_to_write.append("ESTE USUARIO ES DE DEV")
                    write.writerow(row_to_write)
            row_to_write = []
