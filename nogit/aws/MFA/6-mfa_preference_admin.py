import boto3
from pprint import pprint
client = boto3.client('cognito-idp', region_name = 'us-west-2')
response = client.admin_set_user_mfa_preference(
    SMSMfaSettings={
        'Enabled': False,
        'PreferredMfa': False
    },
    SoftwareTokenMfaSettings={
        'Enabled': False,
        'PreferredMfa': False
    },
    Username='sergio.nieto@konfio.mx',
    UserPoolId='us-west-2_PqrIVeNNd' #DEV
    #UserPoolId='us-west-2_VODHRFn7A' #PROD
)
pprint(response)
