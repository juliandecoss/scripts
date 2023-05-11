import boto3
import json
from base64 import b64encode
from hmac import digest

client = boto3.client('cognito-idp', region_name = 'us-west-2')

#client_id ='2jmdtgc74olv85tr1agm3btoi8'
secret = 'mj8m1qlsmm639cu0an7rqa1a0bkpmch05u6g435c6m67v8mh28i'
client_id = '7jgtj79dk97givsn4or6o20d1f'

password = "Test123!"
username = 'ios4@konfio.mx'
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
auth = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    
    AuthParameters={
        "USERNAME": username, "PASSWORD": password, "SECRET_HASH": secret_hash
    },
    ClientId=client_id
)

print(json.dumps(auth, sort_keys=True, indent=4))
""" response_mfa_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='SOFTWARE_TOKEN_MFA',
        Session=auth["Session"],
        ChallengeResponses={
            'USERNAME': username,
            'SOFTWARE_TOKEN_MFA_CODE':"684496",
            'SECRET_HASH': secret_hash,
            'client_id':client_id,
            }
        )

print(json.dumps(response_mfa_challenge, sort_keys=True, indent=4)) """
