import boto3
import json
import pprint
#user_pool_id = 'us-west-2_VODHRFn7A' #prod
user_pool_id = 'us-west-2_PqrIVeNNd' #dev

client = boto3.client('cognito-idp', region_name = 'us-west-2')

def admin_get_user(username: str) -> dict:
    try:
        response = client.admin_get_user(
           UserPoolId=user_pool_id, Username=username
        )
        response["UserAttributes"] = {
            attr["Name"]: attr["Value"] for attr in response["UserAttributes"]
        }
        return response
    except Exception as e:
        print("Exception jeje")
response = admin_get_user("smsprueba@gmail.com")
pprint.pprint(response)
