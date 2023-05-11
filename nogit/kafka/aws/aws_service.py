import boto3


def glue_client():
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
    return session.client("glue")
