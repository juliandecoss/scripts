import boto3
import json
from MFA_CONSTANTS import ACCESS_TOKEN
client = boto3.client('cognito-idp', region_name = 'us-west-2')


response =  client.verify_software_token(
        AccessToken = ACCESS_TOKEN,
        UserCode="378952"
        )

print(json.dumps(response, sort_keys=True, indent=4))