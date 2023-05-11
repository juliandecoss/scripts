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
    new_topic = NewTopic(
        topic=topic_name,
        num_partitions=6,
        config={
            "retention.ms": RETENTION_MS,
        },
    )
    topic_futures = admin.create_topics([new_topic], validate_only=False)
    # Check topic was successfully created
    topic_futures[topic_name].result()
    admin.poll(0)
    print("topic successfully created")


if __name__ == "__main__":
    environ["KAFKA_SERVERS"] = "pkc-pgq85.us-west-2.aws.confluent.cloud:9092"
    environ["KAFKA_SECURITY_PROTOCOL"] = "SASL_SSL"
    environ["KAFKA_SASL_MECHANISM"] = "PLAIN"
    environ["KAFKA_SASL_USERNAME"] = "HMNHCMAFBFLBBHFH"
    environ[
        "KAFKA_SASL_PASSWORD"
    ] = "liGWoy7pAlcHQPKRVufB1txXn/BcOTBG2Bz04mjyv47zGayLZoVKs8VYpdv7Rfcy"
    RETENTION_MS = 604800000  # PARA PROD -> 2419200000
    topic_name = "k-topic-example-api"  # sys.argv[1]
    create_topic(topic_name)
