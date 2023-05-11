import boto3
from botocore.client import Config
from csv import reader, writer

from pprint import pprint

def get_client(service: str, region = 'us-west-2'):
    return boto3.client(
        service, region_name=region, config=Config(signature_version="s3v4")
    )
def get_cognito_client():
    return get_client("cognito-idp")


def get_sso_user_by_email(email: str) -> dict:
    return get_cognito_client().admin_get_user(UserPoolId='us-west-2_VODHRFn7A', Username=email)


with open('./user_admin.csv') as csv_file, open('./usuarios_verificados.csv', 'w') as outFile:
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
            breakpoint()
        if line_count == 5:
            break