import boto3
from botocore.client import Config
from csv import reader, writer

from queries import get_np_id_by_email

def get_client(service: str, region = 'us-west-2'):
    return boto3.client(
        service, region_name=region, config=Config(signature_version="s3v4")
    )
def get_cognito_client():
    return get_client("cognito-idp")


def get_sso_user_by_email(email: str) -> dict:
    return get_cognito_client().admin_get_user(UserPoolId='us-west-2_VODHRFn7A', Username=email)

with open('janin.csv') as csv_file, open('./janin_datos.csv', 'w') as outFile:
    csv_reader = reader(csv_file, delimiter=',')
    write = writer(outFile, delimiter=',')
    attrs = {}
    line_count = -1
    row_to_write = []
    to_print = ""
    for row in csv_reader:
        line_count +=1
        if line_count != 0:
            email =row[0]
            try:
                response = get_sso_user_by_email(email)
                user_status = response.get('UserStatus')
                sso_id = response.get('Username')
            except:
                user_status = ""
            row_to_write.append(email)
            to_print += email+" "
            if not user_status:
                row_to_write.append("ESTE USUARIO NO EXISTE EN SSO")
                to_print += "ESTE USUARIO NO EXISTE EN SSO"+" "
            else:
                row_to_write.append(sso_id)
                row_to_write.append(user_status)
                to_print += sso_id+" "+user_status+" "
            try:
                person = get_np_id_by_email(email)
            except:
                person = None
                row_to_write.append("ESTE USUARIO NO TIENE NP")
                to_print += "ESTE USUARIO NO TIENE NP" +" "
            if person:
                row_to_write.append(person.id)
                to_print += str(person.id) +" "
            write.writerow(row_to_write)
            print(to_print)
            row_to_write = []
            to_print = ""
