from json import dump, loads
from pprint import pprint

import boto3


def get_schema() -> dict:
    sts_client = boto3.client("sts")

    assumed_role_object = sts_client.assume_role(
        RoleArn="arn:aws:iam::726101965919:role/test-users",
        RoleSessionName="julian-test",
    )

    credentials = assumed_role_object["Credentials"]
    pprint(credentials)

    client = boto3.client(
        "glue",
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )
    # response = client.get_schema(
    #     SchemaId={
    #         'SchemaArn': 'arn:aws:glue:us-west-2:726101965919:schema/registryForPoc/schemaForPoc',
    #         #'SchemaName': 'schemaForPoc',
    #         #'RegistryName': 'registryForPoc'
    #     }
    # )

    response = client.get_schema_version(
        # SchemaId={'SchemaArn': 'arn:aws:glue:us-west-2:726101965919:schema/registryForPoc/schemaForPoc'},
        SchemaVersionId="c2a8a188-1547-46c3-a8be-0315c326fd46",
    )
    return response


schema = get_schema()  # ['SchemaDefinition']
schema_name = schema.get("SchemaArn", "").split("/")[-2:-1][0]
schema_json = loads(schema["SchemaDefinition"])

with open(f"{schema_name}.avsc", "w") as fp:
    dump(schema_json, fp, indent=4)
