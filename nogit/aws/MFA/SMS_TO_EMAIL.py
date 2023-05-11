import boto3
import json

client = boto3.client('cognito-idp', region_name = 'us-west-2')
pul='us-west-2_PqrIVeNNd'
name='b2f015a4-8d6f-4186-9c14-0a907c95fa3a'
response = client.admin_list_user_auth_events(
    UserPoolId=pul,
    Username=name,
    MaxResults=60
)