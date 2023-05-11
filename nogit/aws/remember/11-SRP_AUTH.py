import json
import boto3
import hmac, hashlib, base64
from aws_srp import UserAWS
import aws_srp
import json

client = boto3.client('cognito-idp', region_name = 'us-west-2')
user_pool = 'us-west-2_PqrIVeNNd'

client_id = '7jgtj79dk97givsn4or6o20d1f'
user = 'smsprueba@gmail.com'
password = 'Tests@123'
aws = UserAWS(username=user, password=password, pool_id=user_pool, client_id=client_id, client=client)#, client_secret=client_secret,
srp_a = aws_srp.long_to_hex(aws.large_a_value)

response =  client.initiate_auth(
    AuthFlow='USER_SRP_AUTH',
    AuthParameters={
        'USERNAME': user,
        'SRP_A': srp_a
    },
    ClientId=client_id
    )

print(json.dumps(response, sort_keys=True, indent=4))

challenge_responses = aws.process_challenge(response['ChallengeParameters'])
#print(f"Challenge responses used: \n")
#print(challenge_responses)
response_to_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='PASSWORD_VERIFIER',
        ChallengeResponses= challenge_responses
)

print(json.dumps(response_to_challenge, sort_keys=True, indent=4))

""" response_mfa_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='SOFTWARE_TOKEN_MFA',
        Session=response_to_challenge["Session"],
        ChallengeResponses={
            'USERNAME': response["ChallengeParameters"]["USERNAME"],
            'SOFTWARE_TOKEN_MFA_CODE':"847054"
            }
        )
#
print("ULTIMA RESPUESTAS\n")
print(json.dumps(response_mfa_challenge, sort_keys=True, indent=4))

device_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceKey']
device_group_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceGroupKey']
access_token = response_mfa_challenge['AuthenticationResult']['AccessToken']


device_password, device_secret_verifier_config = aws_srp.generate_hash_device(device_group_key, device_key)

print(f"\n\nDEVICE PASSWORD: {device_password}")
print(f"DEVICE SECRET VERIFIER CONFIG: \n {device_secret_verifier_config}\n\n")

response = client.confirm_device(
    AccessToken=access_token,
    DeviceKey=device_key,
    DeviceSecretVerifierConfig=device_secret_verifier_config,
    DeviceName='JulianDevice'
)
print(json.dumps(response, sort_keys=True, indent=4))

response_dev_upd = client.update_device_status(
    AccessToken=access_token,
    DeviceKey=device_key,
    DeviceRememberedStatus='remembered',
)
print(json.dumps(response_dev_upd, sort_keys=True, indent=4)) """