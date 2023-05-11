import sys
from os import environ
from socket import gethostname

from confluent_kafka.admin import AdminClient, NewTopic


def get_conf():
    return {
        "bootstrap.servers": environ["KAFKA_SERVERS"],
        "client.id": gethostname(),
        # "debug": "broker",
        "security.protocol": environ["KAFKA_SECURITY_PROTOCOL"],
        "sasl.mechanism": environ["KAFKA_SASL_MECHANISM"],
        "sasl.username": environ["KAFKA_SASL_USERNAME"],
        "sasl.password": environ["KAFKA_SASL_PASSWORD"],
    }


def create_admin_client() -> AdminClient:
    # Check ACL exists
    conf = get_conf()
    admin = AdminClient(conf)
    return admin


def create_topic(topic_name):
    # Create topic if it doesn't exist
    admin = AdminClient(get_conf())
    available_brokers = len(environ["KAFKA_SERVERS"].split(","))
    new_topic = NewTopic(
        topic=topic_name,
        num_partitions=2,
        replication_factor=available_brokers,
        config={
            "retention.bytes": 2000000,
        },
    )
    topic_futures = admin.create_topics([new_topic], validate_only=False)
    # Check topic was successfully created
    topic_futures[topic_name].result()
    admin.poll(0)
    print("topic successfully created")


if __name__ == "__main__":
    environ[
        "KAFKA_SERVERS"
    ] = "b-1.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096,b-2.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096"
    environ["KAFKA_SECURITY_PROTOCOL"] = "SASL_SSL"
    environ["KAFKA_SASL_MECHANISM"] = "SCRAM-SHA-512"
    environ["KAFKA_SASL_USERNAME"] = "test"
    environ["KAFKA_SASL_PASSWORD"] = "tb6hNQ3P863GaD42U6X2"
    topic_name = sys.argv[1]
    create_topic(topic_name)
