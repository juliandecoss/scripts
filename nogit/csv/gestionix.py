from csv import reader, writer
from db_pymysql.database import database
from queries import get_np_id_by_email
from time import time
import boto3
client = boto3.client('cognito-idp', region_name = 'us-west-2')
with open('emailsfaltantes.csv') as csv_file, open('./new.csv', 'w') as outFile:
    start_time = time()
    csv_reader = reader(csv_file, delimiter=',')
    writer = writer(outFile, delimiter=',')
    line_count = 0
    frase2 = ""
    for row in csv_reader:
        line_count +=1
        email = row[0]
        try:
            response = client.admin_get_user(
                UserPoolId='us-west-2_VODHRFn7A',
                Username=email
            )
            sso_id = response["Username"]
            row.append(sso_id)
            writer.writerow(row)
            print(f"EMAIL => {email} SSO_ID {sso_id}")
        except Exception as e:
            print(f"NO EXISTE => {email}")
            writer.writerow(row)
            print(e.args)
