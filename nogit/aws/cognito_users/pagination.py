import boto3
from pprint import pprint
from time import time_ns
username='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0'
pool_id='us-west-2_PqrIVeNNd' #DEV

client = boto3.client('cognito-idp', region_name = 'us-west-2')
response = client.list_users(
    UserPoolId=pool_id,
    AttributesToGet=['email'],
    Limit=1,
    PaginationToken = 'CAISsAIIARKJAggDEoQCAC+P7iUXcOcC9Tzht7o1iCfsfR6NK8fN/vG4gC7pHWrWeyJAbiI6IlBhZ2luYXRpb25Db250aW51YXRpb25EVE8iLCJuZXh0S2V5IjoiQUFBQUFBQUFCS1VBQVFFQlg2MExNaXBxUTQrTTgwbmNUWm5aUldxQ2p5T0NKRTIwaXZNejlydzVEdU5sYm1ZN2xjMm1vOG5ZNHJHWmpPYUR1Y2p5QUlEQXEvcm9yT1NxdFpEeCtPZk5rOXltNXJ1VXFhYlA0NWpDcnFTZzhzZlZvWmVPdmNEWThnQUJPdz09IiwicHJldmlvdXNSZXF1ZXN0VGltZSI6MTYzNzk1MDM2OTkyMX0aIHRnzypEkyoDIs87YNZRk3dsztpOqChFCr45IxSfnnaj',
    Filter='phone_number = "+529611230729"'
)
pprint(response)