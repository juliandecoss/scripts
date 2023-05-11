from datetime import datetime
from json import loads
from pprint import PrettyPrinter
from AuthHelper import AuthHelper

USER_PASSWORD = 'Tests@123'


def logger(message, value):
    print(f'{5*"="}> {message} <{5*"="}')
    PrettyPrinter(indent=4).pprint(value)


def get_device_data_file_path():
    device_data_filename = "device_data.json"
    file_path = __file__.split("/")
    file_path.pop()
    return f'{"/".join(file_path)}/{device_data_filename}'


def get_challenge_responses(helper, params, device_key=""):
    secret_block = params["SECRET_BLOCK"]
    salt_hex = params["SALT"]
    srp_b_hex = params["SRP_B"]
    username = params.get("USERNAME")
    params_device_key = params.get("DEVICE_KEY", "")
    timestamp = datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
    identity = username
    password = USER_PASSWORD
    if params_device_key:
        #with open(get_device_data_file_path()) as f:
        password = "uF8U8M0pIHe0YFYT2DlnV4/4qXfMBsOSRMFtSxJ0Wv1rs5qLAPO46Q=="
        identity = params_device_key
    claim_signature = helper.get_password_claim_signature(
        identity,
        password,
        helper.hex_to_big_int(srp_b_hex),
        helper.hex_to_big_int(salt_hex),
        secret_block,
        timestamp,
    )
    return {
        "PASSWORD_CLAIM_SIGNATURE": claim_signature,
        "PASSWORD_CLAIM_SECRET_BLOCK": secret_block,
        "TIMESTAMP": timestamp,
        "USERNAME": username,
        "DEVICE_KEY": device_key or params_device_key,
    }