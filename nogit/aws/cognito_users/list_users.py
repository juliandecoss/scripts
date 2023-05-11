import boto3
from pprint import pprint
from time import time_ns
from csv import writer
attr_filter = 'phone_number ^= "+1"'
#pool_id='us-west-2_PqrIVeNNd' #DEV
pool_id='us-west-2_VODHRFn7A' #PROD
times = []
client = boto3.client('cognito-idp', region_name = 'us-west-2')
#
total_users = 0
with open('nogit/cognito/cognito_users/list_user_usa_phone.csv', 'w') as outFile:
    paginationToken = ""
    write = writer(outFile, delimiter=',')
    write.writerow(['email','phone'])
    response = client.list_users(
        UserPoolId=pool_id,
        AttributesToGet=['email','phone_number','phone_number_verified'],
        Limit=60,
        Filter=attr_filter
    )
    paginationToken = response["PaginationToken"]
    for user in response["Users"]:
        for attr in user['Attributes']:
            if attr['Name'] == 'phone_number':
                phone = attr['Value']
            if attr['Name'] == 'phone_number_verified':
                is_verified = attr['Value']
            else:
                email = attr['Value']
        if is_verified != 'false':
            total_users = total_users + 1
            write.writerow([email,phone])
    if paginationToken:
        while True:
            response = client.list_users(
                UserPoolId=pool_id,
                AttributesToGet=['email','phone_number','phone_number_verified'],
                Limit=60,
                PaginationToken=paginationToken,
                Filter=attr_filter,
            )
            for user in response["Users"]:
                for attr in user['Attributes']:
                    if attr['Name'] == 'phone_number':
                        phone = attr['Value']
                    if attr['Name'] == 'phone_number_verified':
                        is_verified = attr['Value']
                    else:
                        email = attr['Value']
                if is_verified != 'false':
                    total_users = total_users + 1
                    write.writerow([email,phone])
            if not response.get("PaginationToken"):
                print(f"Usuarios totaltes {total_users}")
                break
            paginationToken = response["PaginationToken"]
