import boto3
from botocore.exceptions import ClientError
token=""
def update_sso_user(attr):
    try:
        client = boto3.client("cognito-idp", region_name="us-west-2")
        response = client.update_user_attributes(
        UserAttributes=attr,
        AccessToken=token,
        )
        print(response)
    except ClientError as e:
        #print(e.response['Error']['Code'])
        if e.response['Error']['Code'] == 'NotAuthorizedException':
            print("SI LA CACHÉ")
    except Exception as e:
        print(e.args)
sso_user_schema={"email": 'jugui@konfio.com'}
new_user_data = []
for key, value in sso_user_schema.items():
    if value :
        new_user_data.append({"Name": key, "Value": value})

print(new_user_data)
print(update_sso_user(new_user_data))