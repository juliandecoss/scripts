import boto3
import json
from MFA_CONSTANTS import ACCESS_TOKEN
client = boto3.client('cognito-idp', region_name = 'us-west-2')

response =  client.set_user_mfa_preference(
    SoftwareTokenMfaSettings={
        'Enabled': True,
        'PreferredMfa': True
    },
   SMSMfaSettings= {
      "Enabled": False,
      "PreferredMfa": False
   },
    AccessToken = ACCESS_TOKEN
    )

print(json.dumps(response, sort_keys=True, indent=4))
