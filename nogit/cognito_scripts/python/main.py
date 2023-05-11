from argparse import ArgumentParser
from json import loads
from os.path import exists
from time import time_ns

from AuthHelper import AuthHelper
from constants import USER_POOL_ID
from device import confirm_device
from respond_to_auth_challenge import respond_challenge
from srp_init_auth import init_auth
from utils import get_challenge_responses, get_device_data_file_path, logger


def main():
    argsparser = ArgumentParser()
    argsparser.add_argument("--mfaCode", type=str, default="")
    args = argsparser.parse_args()

    user_pool_name = USER_POOL_ID.split("_")[1]
    helper = AuthHelper(user_pool_name)

    device_key = ""
    if exists(get_device_data_file_path()):
        with open(get_device_data_file_path()) as f:
            device_key = loads(f.read())["DeviceKey"]

    response = init_auth(helper, device_key)
    if response.get("ChallengeName", "") == "SOFTWARE_TOKEN_MFA":
        response["ChallengeResponses"] = {
            "USERNAME": response["ChallengeParameters"]["Username"],
            "SOFTWARE_TOKEN_MFA_CODE": args.mfaCode,
        }
        response = respond_challenge(response)
        authentication_result = response["AuthenticationResult"]
        confirm_device(helper, authentication_result)
        response = init_auth(
            helper, authentication_result["NewDeviceMetadata"]["DeviceKey"]
        )
    if response.get("ChallengeName", "") == "DEVICE_SRP_AUTH":
        with open(get_device_data_file_path()) as f:
            device_data = loads(f.read())
        device_group = device_data["DeviceGroupKey"]
        device_key = device_data["DeviceKey"]
        helper = AuthHelper(device_group)
        logger("SRP_A", helper.hex_a)
        response["ChallengeResponses"] = {
            "USERNAME": response["ChallengeParameters"]["Username"],
            "DEVICE_KEY": device_key,
            "SRP_A": helper.hex_a,
        }
        response = respond_challenge(response)
        challenge_name = response["ChallengeName"]
        if challenge_name != "DEVICE_PASSWORD_VERIFIER":
            raise Exception(f"Invalid ChallengeName response: {challenge_name}")
        response["ChallengeResponses"] = get_challenge_responses(
            helper, response["ChallengeParameters"]
        )
        response = respond_challenge(response)

    return response


if __name__ == "__main__":
    start_time = time_ns()
    main()
    logger("Total running time [ms]", (time_ns() - start_time) // 1000000)
