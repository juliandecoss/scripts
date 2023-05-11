import boto3
import json
from aws_srp import UserAWS
import aws_srp
from AuthHelper import AuthHelper
from respond_to_auth_challenge import respond_challenge
from utils import get_challenge_responses

client = boto3.client('cognito-idp', region_name = 'us-west-2')
#client_id = '7jgtj79dk97givsn4or6o20d1f'
client_id ='2jmdtgc74olv85tr1agm3btoi8'
#username = 'smsprueba@gmail.com'
username = 'vamosaver@gmail.com'
password = 'Tests@123'
#user_pool = 'us-west-2_PqrIVeNNd'
#device_key = "us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d"
device_key = 'us-west-2_cee84583-64cf-4c95-beac-60df2de08a78'
auth = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        "USERNAME": username, "PASSWORD": password, "DEVICE_KEY": device_key
    },
    ClientId=client_id
)
print(json.dumps(auth, sort_keys=True, indent=4))
session = auth["Session"]
if auth.get("ChallengeName", "") == "DEVICE_SRP_AUTH":
    """ device_data = {
        "devicePassword" :"uF8U8M0pIHe0YFYT2DlnV4/4qXfMBsOSRMFtSxJ0Wv1rs5qLAPO46Q==",
        "DeviceGroupKey":"-Vfxs5RNW",
        "DeviceKey" : "us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d"
    } """
    device_data = {
        "devicePassword" :"SINmrXmMknQcRwvFQcBXeehZ0wPuYvDdaa7MrZwNxjNVELgcwM7K9w==",
        "DeviceGroupKey":"-tz4QYVVZ",
        "DeviceKey" : "us-west-2_cee84583-64cf-4c95-beac-60df2de08a78"
    }
    device_group = device_data["DeviceGroupKey"]
    device_key = device_data["DeviceKey"]
    device_password = device_data["devicePassword"]
    aws = UserAWS(username=username,device_key=device_key, password=device_password, pool_id=device_group, client_id=client_id, client=client)#, client_secret=client_secret,

    srp_a = aws_srp.long_to_hex(aws.large_a_value)

    response_device_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='DEVICE_SRP_AUTH',
        Session=session,
        ChallengeResponses={
            'USERNAME': username,
            'SRP_A': srp_a,
            'DEVICE_KEY': device_key
            }
        )
    print(json.dumps(response_device_challenge, sort_keys=True, indent=4))
    challenge_responses = aws.process_challenge(response_device_challenge['ChallengeParameters'])

    response_to_challenge =  client.respond_to_auth_challenge(
            ClientId=client_id,
            Session=session,
            ChallengeName='DEVICE_PASSWORD_VERIFIER',
            ChallengeResponses= challenge_responses
    )

    print(json.dumps(response_to_challenge, sort_keys=True, indent=4))
