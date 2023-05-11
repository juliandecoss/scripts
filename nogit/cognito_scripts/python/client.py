from boto3 import client
from botocore.config import Config

cognito = client("cognito-idp", config=Config(region_name="us-west-2"))
