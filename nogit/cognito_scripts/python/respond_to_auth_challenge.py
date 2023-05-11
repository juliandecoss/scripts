from client import cognito
from constants import CLIENT_ID
from utils import logger
from datetime import datetime
import json

def respond_challenge(response):
    challenge_name = response["ChallengeName"]
    params = {
        "ClientId": CLIENT_ID,
        "ChallengeName": challenge_name,
        "ChallengeResponses": response["ChallengeResponses"],
    }
    if "Session" in response:
        params["Session"] = response["Session"]
    print("====================>PASSWORD VERIFIER <=========================")
    print(json.dumps(response["ChallengeResponses"], sort_keys=True, indent=4))
    print(datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y"))
    #f"aws cognito-idp respond-to-auth-challenge --challenge-name PASSWORD_VERIFIER --client-id '7jgtj79dk97givsn4or6o20d1f' --challenge-responses USERNAME='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0',PASSWORD_CLAIM_SECRET_BLOCK={},PASSWORD_CLAIM_SIGNATURE={},DEVICE_KEY={},TIMESTAMP={} --region us-west-2"
    print("====================>    END       <=========================")
    challenge_response = cognito.respond_to_auth_challenge(**params)
    logger(f"{challenge_name} response", challenge_response)
    return challenge_response
