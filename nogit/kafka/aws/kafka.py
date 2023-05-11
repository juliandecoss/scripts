from pprint import pprint

import boto3

sts_client = boto3.client("sts")
pub_poc = "arn:aws:kafka:us-west-2:726101965919:cluster/pub-poc/3eae5233-9514-489d-9778-c0332d3bf0b2-10"
poc = "arn:aws:kafka:us-west-2:726101965919:cluster/poc/6534f954-0590-49f2-8319-f4e5750c640d-10"
# pub_poc = "arn:aws:kafka:us-west-2:726101965919:cluster/micro-poc/0da77eed-8672-4ced-b890-de09d7c56b11-10"
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::726101965919:role/test-users",
    RoleSessionName="julian-test",
)

credentials = assumed_role_object["Credentials"]
kafka_client = boto3.client(
    "kafka",
    aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
)

response = kafka_client.describe_cluster(ClusterArn=poc)
pprint(response)
print(
    "---------------------------------------------------------------------------------------------------------------"
)
response = kafka_client.get_bootstrap_brokers(ClusterArn=poc)
pprint(response)
