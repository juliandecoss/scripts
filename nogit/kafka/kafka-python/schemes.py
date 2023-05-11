import json
from pprint import pprint

import boto3

sts_client = boto3.client("sts")
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::726101965919:role/test-users",
    RoleSessionName="julian-test",
)
credentials = assumed_role_object["Credentials"]
session = boto3.Session(
    aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
    region_name="us-west-2",
)
glue_client = session.client("glue")


with open("account_created_value.avsc", "r") as schema_file:
    schema_str = schema_file.read()
    dict = json.loads(schema_str)
    schema_str_value = json.dumps(dict)

response = glue_client.create_schema(
    RegistryId={
        "RegistryName": "auth",
    },
    SchemaName="k-auth-account-created-value",
    DataFormat="AVRO",
    Compatibility="FULL_ALL",
    Description="Schema for account created topic value",
    Tags={"squad": "platform-services"},
    SchemaDefinition=schema_str_value,
)
pprint(response)
with open("account_created_key.avsc", "r") as schema_file:
    schema_str = schema_file.read()
    dict = json.loads(schema_str)
    schema_str_key = json.dumps(dict)

response = glue_client.create_schema(
    RegistryId={
        "RegistryName": "auth",
    },
    SchemaName="k-auth-account-created-key",
    DataFormat="AVRO",
    Compatibility="FULL_ALL",
    Description="Schema for account created topic key",
    Tags={"squad": "platform-services"},
    SchemaDefinition=schema_str_key,
)
pprint(response)
