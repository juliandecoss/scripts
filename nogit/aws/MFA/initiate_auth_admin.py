import boto3
from base64 import b64encode
from hmac import digest
from pprint import pprint

password = "Tests@123"
username = 'smsprueba@gmail.com'
user_pool = 'us-west-2_PqrIVeNNd'
secret = 'mj8m1qlsmm639cu0an7rqa1a0bkpmch05u6g435c6m67v8mh28i'
client_id = '2v3tko99u3eiid4hie80udvclk'
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
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        "USERNAME": username, "PASSWORD": password, "SECRET_HASH": secret_hash
    }
)
pprint(response)