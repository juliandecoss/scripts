import boto3
import json
import pprint
# MessageAction='RESEND',
#user_pool_id = 'us-west-2_VODHRFn7A' #prod
user_pool_id = 'us-west-2_PqrIVeNNd' #dev
email = 'juligan_2911@hotmail.com'

client = boto3.client('cognito-idp', region_name = 'us-west-2')

response = client.admin_get_user(
    UserPoolId=user_pool_id,
    Username=email
)
#pprint.pprint(response)
sso_id = response["Username"]
#print(f"SSO_ID:{sso_id}")
for attr in response["UserAttributes"]:
    if attr["Name"] == "sub":
        sso = attr["Value"]
        break
print(f"SSO_ID:{sso}")