import boto3
import json
import pprint
# MessageAction='RESEND',
#user_pool_id = 'us-west-2_VODHRFn7A' #prod
user_pool_id = 'us-west-2_PqrIVeNNd' #dev
email = 'konfio-kopayqabot@konfio.mx'
#email = "yusoazul77@hotmail.com"

client = boto3.client('cognito-idp', region_name = 'us-west-2')

response = client.admin_get_user(
    UserPoolId=user_pool_id,
    Username=email
)
pprint.pprint(response,indent=1)
