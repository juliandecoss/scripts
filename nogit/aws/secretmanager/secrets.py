from base64 import b64decode, b64encode
from json import loads
from os import environ

from boto3 import client
from botocore.client import ClientCreator
from botocore.config import Config
from botocore.exceptions import ClientError
from os import environ 
environ["STAGE"] = "dev"
environ["AWS_REGION"] = "us-west-2"

def get_aws_client(service: str) -> ClientCreator:
    return client(service, config=Config(region_name=environ["AWS_REGION"]))

def get_secret_full_name(name: str, base_name: str = "") -> str:
    return f'{environ["STAGE"]}/{base_name or "idp"}/{name}'

def get_secret_value(name: str, base_name: str = "") -> dict:
    return get_aws_client("secretsmanager").get_secret_value(
        SecretId=get_secret_full_name(name, base_name)
    )


def get_secret(name: str, base_name: str = "") -> dict:
    response = get_secret_value(name, base_name)
    return loads(
        response["SecretString"]
        if "SecretString" in response
        else response["SecretBinary"].decode()
    )

subscription_key = get_secret("gestion_subscription_key")
breakpoint()