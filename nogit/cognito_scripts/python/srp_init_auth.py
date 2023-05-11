from constants import USER_PASSWORD, USER_POOL_ID
from client import cognito
from constants import CLIENT_ID, EMAIL
from respond_to_auth_challenge import respond_challenge
from utils import get_challenge_responses, logger
from aws_srp import UserAWS
import json


def init_auth(helper, device_key=""):
    #logger("SRP_A", helper.hex_a)
    #logger("device_key", device_key)
    variables ={
            "USERNAME": EMAIL,
            "SRP_A": helper.hex_a,
            "DEVICE_KEY": device_key,
        }
    auth_response = cognito.initiate_auth(
        ClientId=CLIENT_ID,
        AuthFlow="USER_SRP_AUTH",
        AuthParameters= variables,
    )
    print("====================>SRP INITIATE AUTH PARAMETERS <=========================")
    print(variables)
    print("====================>    END       <=========================")
    print("====================>RESPONSE <=========================")
    print(auth_response)
    print("====================>    END       <=========================")
    #logger("Initiate auth response", auth_response)
    challenge_name = auth_response["ChallengeName"]
    if challenge_name != "PASSWORD_VERIFIER":
        raise Exception(f"Invalid ChallengeName response: {challenge_name}")
    auth_response["ChallengeResponses"] = get_challenge_responses(
        helper, auth_response["ChallengeParameters"], device_key=device_key
    )

    challenge_response = respond_challenge(auth_response)
    challenge_response["ChallengeParameters"]["Username"] = auth_response["ChallengeParameters"]["USERNAME"]
    return challenge_response
