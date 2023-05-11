from utils import logger
import json
import boto3
CLIENT_ID  = '7jgtj79dk97givsn4or6o20d1f'
cognito = boto3.client('cognito-idp', region_name = 'us-west-2')
def respond_challenge(response):
    challenge_name = response["ChallengeName"]
    params = {
        "ClientId": CLIENT_ID,
        "ChallengeName": challenge_name,
        "ChallengeResponses": response["ChallengeResponses"],
    }
    if "Session" in response:
        params["Session"] = response["Session"]
    #print("PARAMSSSSS FOR DEVICE SRP!!!!!!!!!!+++++++++++++++++++++++++++++++++\n")
    challenge_response = cognito.respond_to_auth_challenge(**params)
    #logger(f"{challenge_name} response", challenge_response)
    print(json.dumps(challenge_response, sort_keys=True, indent=4))
    return challenge_response
