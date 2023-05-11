import base64
import hashlib
import hmac

import boto3

import aws_srp
from aws_srp import UserAWS

client = boto3.client("cognito-idp", region_name="us-west-2")

user_pool = "us-west-2_PqrIVeNNd"
client_id = "2v3tko99u3eiid4hie80udvclk"
client_secret = "mj8m1qlsmm639cu0an7rqa1a0bkpmch05u6g435c6m67v8mh28i"
user = "4307f412-e581-449a-89c8-c9edd93fcc0a"
password = "Tests@123"
phone = "+525549490369"

message = bytes(user + client_id, "utf-8")
key = bytes(client_secret, "utf-8")
secret_hash = base64.b64encode(
    hmac.new(key, message, digestmod=hashlib.sha256).digest()
).decode()

aws = UserAWS(
    username=user,
    password=password,
    pool_id=user_pool,
    client_id=client_id,
    client_secret=client_secret,
    client=client,
)
srp_a = aws_srp.long_to_hex(aws.large_a_value)

response = client.initiate_auth(
    AuthFlow="USER_SRP_AUTH",
    AuthParameters={"USERNAME": user, "SECRET_HASH": secret_hash, "SRP_A": srp_a},
    ClientId=client_id,
)

print(f"Secret used:{secret_hash}\n")
# print(json.dumps(response, sort_keys=True, indent=4))

print("Creating payload for next step ...\n")

challenge_responses = aws.process_challenge(response["ChallengeParameters"])

print(f"Challenge responses used: \n")
print(challenge_responses)
response_to_challenge = client.respond_to_auth_challenge(
    ClientId=client_id,
    ChallengeName="PASSWORD_VERIFIER",
    Session="my_session_my_session",
    ChallengeResponses=challenge_responses,
)

# print(response_to_challenge)
