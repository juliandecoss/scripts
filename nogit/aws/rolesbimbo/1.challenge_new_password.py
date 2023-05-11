import boto3
import json
from base64 import b64encode
from hmac import digest


client_id ='2v3tko99u3eiid4hie80udvclk'
secret = 'mj8m1qlsmm639cu0an7rqa1a0bkpmch05u6g435c6m67v8mh28i'
username = 'juligan_2911@hotmail.com'
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
response_mfa_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='NEW_PASSWORD_REQUIRED',
        Session="AYABePaFdx_xPmitzIdqKBs_w7MAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjowMTU3MzY3MjcxOTg6a2V5LzI5OTFhNGE5LTM5YTAtNDQ0Mi04MWU4LWRkYjY4NTllMTg2MQC4AQIBAHiLcRcG62Mb19KUM6qQUoajwNOF_-4FakXKLIP1RcBYjQEo74vI1ZWZdUHTatoPgCBtAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMPnTOTzXXDQ22p_G6AgEQgDuCxu3VMPG3elTHfUXP89cRwKN_yyb0WL0NjecGfOTQKdbd_bH9bq4phakeCABl3g0hI-f2O28tyENKzwIAAAAADAAAEAAAAAAAAAAAAAAAAAB0HC0iWVXTBBohohUmIEyU_____wAAAAEAAAAAAAAAAAAAAAEAAADVH8fyo6echpexXnwhjtfAE5Cz6dxYy27YER9QUbzKCtLrf3eMK4cnDgdIe02H_571-kREUMY6O7Kg5cUiSgnMxhFzdo-x1jAI8Gs7xC4hHLWkeeXd93EqMbe9fprxEgQgdLl-DVy8Gbipo1dFZWbU6wrD3IxDhDkajBcdaJGw6voOv4h0HJ3Y0uDiM1zfCBsVrl0ImB5ln_sCvNKyDZOUs9Np6gxLozNRkHsE-pphWTjNtmBPPmVs3IOdekfvfo05NDM5JClTJsoxW4mHsg_E50CFUPFyM05fxutH37Vg-6E93nFZ-w",
        ChallengeResponses={
            'USERNAME': username,
            'NEW_PASSWORD':"Tests@123",
            "SECRET_HASH": secret_hash
            }
        )

print(json.dumps(response_mfa_challenge, sort_keys=True, indent=4))