import boto3
import pprint
from datetime import date, datetime
client = boto3.client('cognito-idp', region_name = 'us-west-2')
user_pool_id = 'us-west-2_PqrIVeNNd'
#user_pool_id = "us-west-2_SGHXfzcyN"
email = 'decossjulian@gmail.com'
response = client.admin_delete_user(
    UserPoolId=user_pool_id,
    Username=email
)
pprint.pprint(response)
