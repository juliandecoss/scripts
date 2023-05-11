from pprint import pprint

import boto3
from aws_schema_registry import SchemaRegistryClient
from aws_schema_registry.adapter.kafka import KafkaDeserializer

from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic, deserializer: KafkaDeserializer):
        self.consumer = KafkaConsumer(
            topic,
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            bootstrap_servers=[
                "b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196"
            ],
            api_version=(2, 6, 2),
            sasl_plain_username="test",
            sasl_plain_password="tb6hNQ3P863GaD42U6X2",
            value_deserializer=deserializer,
            auto_offset_reset="earliest",
            consumer_timeout_ms=10000,
            # ssl_cafile="truststore.pem",
        )

    def star_read(self):
        self.receive_message()

    def receive_message(self):
        message_count = 0
        for message in self.consumer:
            message = message.value
            data = message[0]
            schema = message[1]
            # print(f"Message {message_count}: {message}")
            print(f"Data:  \n")
            pprint(data)
            print(f"Schema:")
            pprint(schema)
            message_count += 1

    def poll_message(self):
        self.consumer.commit_async()
        a = self.consumer.poll()
        return a

    def check(self):
        a = self.consumer.partitions_for_topic("first-topic")
        return a


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
deserializer = KafkaDeserializer(client)
consumer = Consumer("first-topic", deserializer)

consumer.star_read()
# consumer.loquequiera()
