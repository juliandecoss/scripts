from pprint import pprint

import boto3

sts_client = boto3.client("sts")

assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::726101965919:role/test-users",
    RoleSessionName="julian-test",
)

credentials = assumed_role_object["Credentials"]
pprint(credentials)
