from calendar import c
import boto3
from pprint import pprint
from time import time_ns
from csv import writer
attr_filter = 'cognito:user_status = "FORCE_CHANGE_PASSWORD"'
username='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0'
#pool_id='us-west-2_PqrIVeNNd' #DEV
pool_id='us-west-2_VODHRFn7A' #PROD

client = boto3.client('cognito-idp', region_name = 'us-west-2')
def with_pagination(pagination_token):
    return client.list_users(
        UserPoolId=pool_id,
        AttributesToGet=['email'],
        Limit=60,
        PaginationToken=pagination_token,
        Filter=attr_filter
    )
response = client.list_users(
    UserPoolId=pool_id,
    AttributesToGet=['email'],
    Limit=60,
    Filter=attr_filter
)

with open('./cognito_users/force_status_users.csv', 'w') as outFile:
    write = writer(outFile, delimiter=',')
    row_to_write = []
    to_print = ""
    row_to_write.append("email")
    row_to_write.append("status")
    row_to_write.append("creationDate")
    write.writerow(row_to_write)
    row_to_write = []
    for user in response["Users"]:
        email = user["Attributes"][0]["Value"]
        row_to_write.append(email)
        row_to_write.append(user['UserStatus'])
        row_to_write.append(user['UserCreateDate'])
        write.writerow(row_to_write)
        row_to_write = []
    requires_searchin = False
    pagination_t = response.get("PaginationToken","")
    if pagination_t and len(response["Users"]) > 0:
        print("Primera pagina")
        print(f"En la pagina hay {len(response['Users'])} usuarios")
        requires_searchin = True
    while requires_searchin == True:
        response = with_pagination(pagination_t)
        print("Cambiamos de pagina")
        print(f"En la pagina hay {len(response['Users'])} usuarios")
        pagination_t = response.get("PaginationToken","")
        if len(response["Users"]) > 0:
            for user in response["Users"]:
                email = user["Attributes"][0]["Value"]
                row_to_write.append(email)
                row_to_write.append(user['UserStatus'])
                row_to_write.append(user['UserCreateDate'])
                write.writerow(row_to_write)
                row_to_write = []
        if len(response["Users"])<60:
            print(f"Ultima pagina pagination token es:{pagination_t}")
            break
            
