import boto3
from base64 import b64encode
from hmac import digest
from pprint import pprint

password = "zyA?jB8z)v5xOEp_"
username = 'juliandecoss@konfio.mx'
user_pool = 'us-west-2_SGHXfzcyN'
secret = '2ifl1526n8rb6b23st3fd8u4khr9b5405ljqv7crpvbbd6iiasb'
client_id = '2cs85dtq1ntnjnrbtt8bau7me5'
app_data = {"id":client_id,"secret":secret,"username":username}
def generate_secret_hash(app_client_data: dict) -> str:
    return b64encode(
        digest(
            key=app_client_data["secret"].encode(),
            msg=(app_client_data["username"] + app_client_data["id"]).encode(),
            digest="sha256",
        )
    ).decode()
secret_hash = generate_secret_hash(app_data)
client = boto3.client('cognito-idp', region_name = 'us-west-2')
response = client.admin_initiate_auth(
    UserPoolId=user_pool,
    ClientId=client_id,
    AuthFlow='ADMIN_USER_PASSWORD_AUTH',
    AuthParameters={
        "USERNAME": username, "PASSWORD": password, "SECRET_HASH": secret_hash
    }
)
pprint(response)