from os import environ

from boto3 import client
from botocore.config import Config


def get_aws_client(service: str):
    return client(
        service, config=Config(region_name=environ.get("AWS_REGION", "us-west-2"))
    )


def get_cognito_client():
    return get_aws_client("cognito-idp")


def get_parameters_by_path(
    path: str, decrypted: bool = False, recursive: bool = False
) -> dict:
    ssm = get_aws_client("ssm")
    return ssm.get_parameters_by_path(
        Path=path, WithDecryption=decrypted, Recursive=recursive
    )


def get_params_values(
    path: str, decrypted: bool = False, recursive: bool = False
) -> dict:
    data = get_parameters_by_path(path, decrypted=decrypted, recursive=recursive)
    response = {}
    if data and "Parameters" in data:
        for elem in data["Parameters"]:
            key = elem.get("Name", "").replace(f"{path}/", "")
            response[key] = elem.get("Value")
    return response

param_store_data = get_params_values(
        f"/dev/platform/sso/gestionix", decrypted=True, recursive=True
    )
print(param_store_data)