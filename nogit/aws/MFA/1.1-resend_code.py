
import boto3
import json

client = boto3.client('cognito-idp', region_name = 'us-west-2')
response = client.resend_confirmation_code(
    ClientId='7jgtj79dk97givsn4or6o20d1f',
    Username='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0',
   
)
""" UserContextData={
        'EncodedData': 'string'
    },
AnalyticsMetadata={
    'AnalyticsEndpointId': 'string'
},
ClientMetadata={
    'string': 'string'
} """