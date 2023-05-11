from csv import reader, writer
from boto3 import client
from botocore.config import Config
cognito = client("cognito-idp", config=Config(region_name="us-west-2"))
print(cognito.admin_get_user(
    UserPoolId="us-west-2_VODHRFn7A",
    Username="test@konfio.mx",
))