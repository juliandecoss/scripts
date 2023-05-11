import boto3
import aws_srp
from aws_srp import UserAWS

client = boto3.client('cognito-idp', region_name = 'us-west-2')
client_id = '7jgtj79dk97givsn4or6o20d1f'
pool_id = 'us-west-2_PqrIVeNNd'
client_secret = None
username = "testeslabuena@ahorasi.com"
password = "1234$Contra"

aws = UserAWS(username=username, password=password, pool_id=pool_id,
                client_id=client_id, client_secret=client_secret, client=client)

auth = client.initiate_auth(
    AuthFlow='USER_SRP_AUTH',
    AuthParameters={
        "USERNAME": username, "SRP_A": aws_srp.long_to_hex(aws.large_a_value)
    },
    ClientId=client_id
)

print(f"\nCLIENT AUTH: \n\n {auth}\n\n")

cr = aws.process_challenge(auth['ChallengeParameters'])
response_2_challenge = client.respond_to_auth_challenge(
    ClientId=client_id,
    ChallengeName=auth['ChallengeName'],
    ChallengeResponses=cr
)

print(f"\nRESPONSE PASSWORD VERIFIER: \n\n {response_2_challenge}\n\n")

response_mfa_challenge = client.respond_to_auth_challenge(
    ClientId = client_id,
    Session = response_2_challenge["Session"],
    ChallengeName="SOFTWARE_TOKEN_MFA",
    ChallengeResponses= {
        "USERNAME": auth["ChallengeParameters"]["USERNAME"],
        "SOFTWARE_TOKEN_MFA_CODE": "195353"
    }
)

print(f"\nRESPONSE MFA CHALLENGE: \n\n {response_mfa_challenge}\n\n")

device_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceKey']
device_group_key = response_mfa_challenge['AuthenticationResult']['NewDeviceMetadata']['DeviceGroupKey']
access_token = response_mfa_challenge['AuthenticationResult']['AccessToken']

print(f"\n\nDEVICE KEY: {device_key}\n")
print(f"DEVICE GROUP: {device_group_key}\n")
print(f"ACESS TOKEN: {access_token}\n\n")

# 3. Generate random device password, device salt and verifier
device_password, device_secret_verifier_config = aws_srp.generate_hash_device(device_group_key, device_key)

print(f"\n\nDEVICE PASSWORD: {device_password}")
print(f"DEVICE SECRET VERIFIER CONFIG: \n {device_secret_verifier_config}\n\n")

confirm_device = client.confirm_device(
    AccessToken=access_token,
    DeviceKey=device_key,
    DeviceSecretVerifierConfig=device_secret_verifier_config,
    DeviceName='KerrycoQuebab2222',
)

print(f"\n\nCONFIRM DEVICE: \n{confirm_device}\n\n")

# 4. Remember the device
response_dev_upd = client.update_device_status(
    AccessToken=access_token,
    DeviceKey=device_key,
    DeviceRememberedStatus='remembered',
)

print(f"\n\nREMEMBER DEVICE: \n{response_dev_upd}\n\n")
