import boto3
from pprint import pprint

username='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0'
pool_id='us-west-2_PqrIVeNNd' #DEV
#pool_id='us-west-2_VODHRFn7A' #PROD

client = boto3.client('cognito-idp', region_name = 'us-west-2')

# response = client.admin_enable_user(
#     UserPoolId=pool_id,
#     Username='juligan_2911@hotmail.com'
# )

response = client.admin_disable_user(
    UserPoolId=pool_id,
    Username='karinarojom@gmail.com'
)
pprint(response)