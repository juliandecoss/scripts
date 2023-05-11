from csv import reader, writer
from boto3 import client
from botocore.config import Config
from time import time
from json import dumps

cognito = client("cognito-idp", config=Config(region_name="us-west-2"))

with open('./KonfioERPUser.csv', newline='') as orignal, open('./new.csv', 'w') as outFile:
    start_time = time()
    reader = reader(orignal, delimiter=',')
    writer = writer(outFile, delimiter=',')
    headers = next(reader)
    headers.append("SsoId")
    writer.writerow(headers)
    new_rows = []
    for row in reader:
        _, email = row
        response = cognito.admin_get_user(
            UserPoolId="us-west-2_VODHRFn7A",
            Username=email,
        )
        row.append(response.get("Username"))
        new_rows.append(row)
    print(time() - start_time)
    for row in new_rows:
        writer.writerow(row)
    print(time() - start_time)