import boto3
from botocore.client import Config
from csv import reader, writer
from db_pymysql.database import database
from queries import get_np_id_by_email
from time import time
NP_IDS = []
def get_client(service: str, region = 'us-west-2'):
    return boto3.client(
        service, region_name=region, config=Config(signature_version="s3v4")
    )
def get_cognito_client():
    return get_client("cognito-idp")

def get_sso_user_by_email(email: str) -> dict:
    return get_cognito_client().admin_get_user(UserPoolId='us-west-2_VODHRFn7A', Username=email)

""" with open('emailsfaltantes.csv') as csv_file, open('./new.csv', 'w') as outFile:
    start_time = time()
    csv_reader = reader(csv_file, delimiter=',')
    writer = writer(outFile, delimiter=',')
    line_count = 0
    frase2 = ""
    for row in csv_reader:
        line_count +=1
        email = row[0]
        #np_id = database(args=row[1])
        #np_id = get_np_id_by_email(row[1])
        #if not np_id:
            #np_id = 'NULL'
            #np_id = np_id["id"]
            #np_id = np_id
        #else:
           # 
        #row.append(np_id)
        frase = f" or email = '{email}' or userName = '{email}'"
        frase2 = frase2+ frase
        #writer.writerow(row)
        #if line_count == 50:
           # print(time() - start_time)
           # break
    print(frase2)
    #writer.writerow(frase2) """
try:
    attrs = {}
    response = get_sso_user_by_email("d0c49154-cebf-4924-a480-a76423069af1")
    user_data = response.get("UserAttributes") or []
except:
    user_data = ""
else:
    for attr in user_data:
        attrs[attr["Name"]] = attr["Value"]
    email = attrs['email'] 
    print(email)
    print(attrs)
    try:
        person = get_np_id_by_email(email)
    except:
        person = None

    print(person)