import json

import boto3
from aws_schema_registry import SchemaRegistryClient
from aws_schema_registry.adapter.kafka import KafkaSerializer
from aws_schema_registry.avro import AvroSchema

from kafka import KafkaProducer

# ssl_cafile='truststore.pem',


class Producer:
    def __init__(
        self, topic, value_serializer: KafkaSerializer, key_serializer: KafkaSerializer
    ):
        self.topic = topic
        self.producer = KafkaProducer(
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            bootstrap_servers="b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196",
            api_version=(2, 6, 2),
            sasl_plain_username="test",
            sasl_plain_password="tb6hNQ3P863GaD42U6X2",
            value_serializer=value_serializer,
            key_serializer=key_serializer,
        )

    def star_write(
        self, schema: AvroSchema, data: dict, key_data: dict, key_schema: AvroSchema
    ):

        self.producer.send(self.topic, value=(data, schema), key=(key_data, key_schema))


def main():
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
    client = SchemaRegistryClient(glue_client, registry_name="registryForPoc")
    serializer = KafkaSerializer(client)
    producer = Producer("first-topic", serializer)
    with open("registryForPoc.avsc", "r") as schema_file:
        schema_str = schema_file.read()
        dict = json.loads(schema_str)
        schema = AvroSchema(dict)
    data = {
        "user_id": 4,
        "natural_person_id": 6,
        "enterprise_id": 7,
        "source": "nolosabemos",
    }
    producer.star_write(schema, data)
    print("THE DATA HAS BEEN SENT")


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    main()
