import boto3
import json
import aws_srp
from base64 import b64encode
from hmac import digest
client = boto3.client('cognito-idp', region_name = 'us-west-2')
user_pool = 'us-west-2_PqrIVeNNd'

client_id = '7jgtj79dk97givsn4or6o20d1f'
user = 'smsprueba@gmail.com'
password = 'Tests@123'
#app_data = {"id":client_id,"secret":secret,"username":username}

def generate_secret_hash(app_client_data: dict) -> str:
    return b64encode(
        digest(
            key=app_client_data["secret"].encode(),
            msg=(app_client_data["username"] + app_client_data["id"]).encode(),
            digest="sha256",
        )
    ).decode()

#secret_hash = generate_secret_hash(app_data)
response_mfa_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='SMS_MFA',
        Session="AYABePg7u_TmXgHOsd10-UwtGd8AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjowMTU3MzY3MjcxOTg6a2V5LzI5OTFhNGE5LTM5YTAtNDQ0Mi04MWU4LWRkYjY4NTllMTg2MQC4AQIBAHiLcRcG62Mb19KUM6qQUoajwNOF_-4FakXKLIP1RcBYjQE37Qq8yDO9o6mp8nu-dAtHAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMfzf-C0a2u1qZAQAQAgEQgDtNtlAH43XFPsPUl2ydehNalKpbgfbOpvASvi4n1GGy3pTLI97rzF995DI_3T3ikuDlhCFB7fUJW4YjYAIAAAAADAAAEAAAAAAAAAAAAAAAAABaWfilEmcYQJWIeGnJubra_____wAAAAEAAAAAAAAAAAAAAAEAAAIA6yYBvw-qMA1j3YMVeTLZ0F46nRahY2mXm6tcyDabHuoSO6vhDiRpyG8ivdhVl1fc2-9diT6AfktGpUSGswMbrFYDW4-NqkGyIODuZ3s_PApMMpCvp7u8-57o7br9hDfOvnusGiJDwJ-SjBlu8LfSSnfpXoh4yGDMNhN5xTLp6qcICuZV0BwEgaWXMLe42nhPf1wr_-14SaRVynBdIP64_A-QHDaBrqjTi5fzPJPgTgwM88zKOrnQD0qC3lBtkaSbxg2RPUVbQvFWIpnEmn8ayga2dZKbMTQHYxbYKJslfvmXbLXd9xAnfLlh1VdwOg7TTIFhMreWGiyuKJfHmGqr5IS9o2zebz8miU-WB_cfkSkz3IuDBz7cUiaeIWvTo26MpLnZWwDvO52CqxsDqcayHq6QxOieMFCkzYX75pEP2nK5dVEBMM3fAz4A8Ktk1G1VStPOydWzMw0xEQfH4bDbCbzbW4bOdmQbxcfoiUk4U3P5M8U-BarHBDn0vG8hsArrX-H6IaSvdYQlIsOLbtyOHP2nw0MXhMlg2gyp8MUqN35QwJ1OJoqZLQX-w3CYtyisTxfg0qezXzj7KJF1oXEindAy8JlvD2swyrzxa8GE-JtpCuKAgn2pwmHI6ijaul_y9-TXLM-j6dp_G6kZvWZ-MqoOgIbcn7i2o8iZLDcD2QuAzNhsjzImsVOYLdnDGfQR",
        ChallengeResponses={
            'USERNAME': "23daf9dd-117d-48f0-9a41-3ed5fd6a74b0",
            'SMS_MFA_CODE':"420875",
            }
        )

print("ULTIMA RESPUESTAS\n")
print(json.dumps(response_mfa_challenge, sort_keys=True, indent=4))
breakpoint()
device_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceKey']
device_group_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceGroupKey']
access_token = response_mfa_challenge['AuthenticationResult']['AccessToken']


device_password, device_secret_verifier_config = aws_srp.generate_hash_device(device_group_key, device_key)

print(f"\n\nDEVICE PASSWORD: {device_password}")
print(f"\nDEVICE KEY {device_key}")
print(f"\nDevice Group {device_group_key}")
#print(f"DEVICE SECRET VERIFIER CONFIG: \n {device_secret_verifier_config}\n\n")

response = client.confirm_device(
    AccessToken=access_token,
    DeviceKey=device_key,
    DeviceSecretVerifierConfig=device_secret_verifier_config,
    DeviceName='PRUEBAS DE LOCAL'
)
print(json.dumps(response, sort_keys=True, indent=4))
