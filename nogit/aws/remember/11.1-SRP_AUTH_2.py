import json
import boto3
import hmac, hashlib, base64
import datetime
from aws_srp import UserAWS
import aws_srp
import json

client = boto3.client('cognito-idp', region_name = 'us-west-2')
user_pool = 'us-west-2_PqrIVeNNd'
user='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0'
password='Tests@123'
phone='+529611230729'
client_id = '7jgtj79dk97givsn4or6o20d1f'

aws = UserAWS(username=user, password=password, pool_id=user_pool, client_id=client_id, client=client)
srp_a = aws_srp.long_to_hex(aws.large_a_value)
#device_key = "us-west-2_6a7cbfc2-fe01-4e07-9c57-0e9d0432f96a"
device_key =  "us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d"
response =  client.initiate_auth(
    AuthFlow='USER_SRP_AUTH',
    AuthParameters={
        'USERNAME': "35665ff1-41ed-4130-9555-8a40fdf7d517",
        'SRP_A': srp_a,
        #'DEVICE_KEY': "us-west-2_6a7cbfc2-fe01-4e07-9c57-0e9d0432f96a"
        'DEVICE_KEY' :  "us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d"
    },
    ClientId=client_id
    )
print(json.dumps(response, sort_keys=True, indent=4))

challenge_responses = aws.process_challenge(response['ChallengeParameters'])
challenge_responses["DEVICE_KEY"] = device_key

response_to_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='PASSWORD_VERIFIER',
        ChallengeResponses= challenge_responses
)
print(json.dumps(response_to_challenge, sort_keys=True, indent=4))
aws = UserAWS(username=user, password=password, pool_id=user_pool, client_id=client_id, client=client)
srp_a = aws_srp.long_to_hex(aws.large_a_value)
response_device_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='DEVICE_SRP_AUTH',
        Session=response_to_challenge["Session"],
        ChallengeResponses={
            'USERNAME': '23daf9dd-117d-48f0-9a41-3ed5fd6a74b0',
            'SRP_A': srp_a,
            'DEVICE_KEY': device_key
            }
        )

print(json.dumps(response_device_challenge, sort_keys=True, indent=4))
#response_device_challenge
#challenge_responses = aws.second_process_challenge(response_device_challenge['ChallengeParameters'])
#challenge_responses["DEVICE_KEY"] = "us-west-2_22b0baeb-b293-4a7d-924c-61ca03cd3e54"

""" response_device_to_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='DEVICE_PASSWORD_VERIFIER',
        Session="AYABeCWFIqbWRgBSsNA_yrqakMQAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjowMTU3MzY3MjcxOTg6a2V5LzI5OTFhNGE5LTM5YTAtNDQ0Mi04MWU4LWRkYjY4NTllMTg2MQC4AQIBAHiLcRcG62Mb19KUM6qQUoajwNOF_-4FakXKLIP1RcBYjQFHKluVpTwUnxzTaMu-uBv9AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM_nBkbU8uKPm7t6SAAgEQgDsVv-wlbGV1XifY3maNs4Hl8BmqGa5Zs0E2uMR8S4cLU0Yr5ieurARQxiC4ncJowzr2atJ0ryz-9XJNGgIAAAAADAAAEAAAAAAAAAAAAAAAAACoCcdaKE5hicvGcR7vbUNy_____wAAAAEAAAAAAAAAAAAAAAEAAAEBaGP3HkoDvFQsQSHuAPpHqjBGsO1ABLgLzd2aYsaAdQZxl0kf1jmzfyqNWdR0796QLNjoA7VedEUakeW06xMPBxD0OSsFOdGdX5ukmYs1I6dIVTkCNmAgr2tdEDiv2BiN7fLEIBLKjnOeWNkLQKpxSgc0cbg4hzJEdxFSUQhYw1JtS0hElbyua8GV3jSGi-S3paul_fcDXaB0hfDnz6sMPVk_brCgHP3sR4YD23zx5biOC76XF3o60vAV-NA8AX_LZN2KyiGmFuqvm0KMvQjyExz-A-F92dwqHadfYla6N6YrB8XugwyKghi_Z8WwykoUCI3el0ek9VY0P8n74s-7UFq12xy_krHyzqOnj7oJ6AgO",
        ChallengeResponses= challenge_responses
) """



""" challenge_params = response_device_challenge['ChallengeParameters']
challenge_params['USER_ID_FOR_SRP'] = challenge_params['USERNAME']
cr2 = aws.second_process_challenge(challenge_params)

response2 = client.respond_to_auth_challenge(
    ClientId=client_id,
    ChallengeName='DEVICE_PASSWORD_VERIFIER',
    ChallengeResponses=cr2
) """
"""
{
        'USERNAME': "b0a7a786-c0d5-4a6d-b136-25902bd32098",
        'PASSWORD_CLAIM_SECRET_BLOCK': response['ChallengeParameters']['SECRET_BLOCK'],
        'TIMESTAMP': datetime.datetime.utcnow().strftime( "%a %b %d %H:%M:%S UTC %Y").upper(),
        'PASSWORD_CLAIM_SIGNATURE': cr2['PASSWORD_CLAIM_SIGNATURE'],
        'DEVICE_KEY': "us-west-2_22b0baeb-b293-4a7d-924c-61ca03cd3e54"
    }
"""
""" print("ULTIMA RESPUESTAS\n")
print(json.dumps(response2, sort_keys=True, indent=4)) """