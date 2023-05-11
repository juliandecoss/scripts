import boto3
from botocore.exceptions import ClientError
from pprint import pprint
try:
    client = boto3.client("cognito-idp", region_name="us-west-2")
    response = client.admin_update_user_attributes(
        UserPoolId='us-west-2_PqrIVeNNd',
        Username='ekruk@srpago.com',
        UserAttributes=[
            {
                'Name': 'phone_number',
                'Value': '+5493758409759',
            }
        ]
    )
    pprint(response)
except ClientError as e:
        if e.response['Error']['Code'] == 'UserNotFoundException':
            print("USUARIO NO EXISTE")
except Exception as e:
    print(e.args)