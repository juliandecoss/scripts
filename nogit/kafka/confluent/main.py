from base64 import b64encode
from os import environ
from random import randint
from secrets import token_urlsafe
from socket import gethostname

from confluent_kafka import Consumer, KafkaError, Producer
from confluent_kafka.admin import (AclBinding, AclBindingFilter, AclOperation,
                                   AclPermissionType, AdminClient, NewTopic,
                                   ResourcePatternType, ResourceType)


def logger(action, msg):
    print("*" * 10, f"{action}:\n", msg)


def get_conf():
    return {
        "bootstrap.servers": environ["KAFKA_SERVERS"],
        "client.id": gethostname(),
        #"debug": "broker",
        "security.protocol": environ["KAFKA_SECURITY_PROTOCOL"],
        "sasl.mechanism": environ["KAFKA_SASL_MECHANISM"],
        "sasl.username": environ["KAFKA_SASL_USERNAME"],
        "sasl.password": environ["KAFKA_SASL_PASSWORD"],
    }


def create_topic(topic_name):
    # Create AdminClient and connect to Kafka
    conf = get_conf()
    admin = AdminClient(conf)

    # Check topic exists
    cluster_metadata = admin.list_topics(topic=topic_name)
    topics = cluster_metadata.topics
    logger("topics", topics)
    topic_metadata = topics.get(topic_name)
    if not all([topics, topic_metadata]) or isinstance(
        topic_metadata.error, KafkaError
    ):
        logger("topic metadata error", topic_metadata.error.str())
        error_name = topic_metadata.error.name()
        if error_name in ["TOPIC_AUTHORIZATION_FAILED"]:
            raise Exception("Unauthorized access to user")
        elif error_name in ["UNKNOWN_TOPIC_OR_PART"]:
            # Check ACL exists
            acl_name = "kafka-cluster"
            acl_filter = AclBindingFilter(
                restype=ResourceType.ANY,
                name=None,
                resource_pattern_type=ResourcePatternType.ANY,
                principal=None,
                host=None,
                operation=AclOperation.ANY,
                permission_type=AclPermissionType.ANY,
            )
            acls_future = admin.describe_acls(acl_binding_filter=acl_filter)
            acls = acls_future.result()
            logger("ACLs", acls)
            splitted_broker_name = cluster_metadata.orig_broker_name.split(".")
            broker_dns = ".".join(splitted_broker_name[1:-1]) + ".com"
            for acl in acls:
                broker_acl_exists = acl.name == acl_name and broker_dns in acl.principal
                if broker_acl_exists:
                    break
            if not acls:  # or not broker_acl_exists
                # Create brokers ACL
                broker_acls = [
                    AclBinding(
                        restype=restype,
                        name=acl_name if restype == ResourceType.BROKER else "*",
                        resource_pattern_type=ResourcePatternType.LITERAL,
                        principal=f"User:CN=*.{broker_dns}",
                        host="*",
                        operation=AclOperation.ALL,
                        permission_type=AclPermissionType.ALLOW,
                    )
                    for restype in [
                        ResourceType.BROKER,
                        ResourceType.TOPIC,
                        ResourceType.GROUP,
                    ]
                ]
                acl_futures = admin.create_acls(broker_acls)
                # Check ACLs were successfully created
                for future in acl_futures.values():
                    future.result()

        # Create topic if it doesn't exist
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


def produce_to_topic(topic_name):
    # Create Producer and connect to Kafka
    conf = get_conf()
    producer = Producer(conf)
    messages = [token_urlsafe() for _ in range(0, randint(4, 9))]
    logger("messages produced", messages)
    key = b64encode(topic_name.encode()).decode()
    for message in messages:
        producer.produce(
            topic=topic_name,
            key=key,
            value=message,
        )
    producer.poll(0)
    producer.flush()


def consume_topic(topic_name):
    conf = get_conf()
    conf.update(
        {
            "group.id": "default",
            "auto.offset.reset": "earliest",
        }
    )
    consumer = Consumer(conf)
    consumer.subscribe([topic_name])
    while True:
        message = consumer.poll(1.0)
        if message:
            logger("message", message.value())


def main():
    topic_name = "first-topic2"
    create_topic(topic_name)
    # produce_to_topic(topic_name)
    # consume_topic(topic_name)


if __name__ == "__main__":
    environ[
        "KAFKA_SERVERS"
    ] = "b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196,b-2-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196"
    environ["KAFKA_SECURITY_PROTOCOL"] = "SASL_SSL"
    environ["KAFKA_SASL_MECHANISM"] = "SCRAM-SHA-512"
    environ["KAFKA_SASL_USERNAME"] = "test"
    environ["KAFKA_SASL_PASSWORD"] = "tb6hNQ3P863GaD42U6X2"
    main()
