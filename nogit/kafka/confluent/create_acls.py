from os import environ
from socket import gethostname

from confluent_kafka.admin import (AclBinding, AclOperation, AclPermissionType,
                                   AdminClient, ResourcePatternType,
                                   ResourceType)


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


def create_acls():
    admin = AdminClient(get_conf())
    broker_dns = "poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com"
    acl_name = "kafka-cluster"
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

    """user_acls = [
            AclBinding(
                restype=restype,
                name=acl_name if restype == ResourceType.BROKER else "*",
                resource_pattern_type=ResourcePatternType.LITERAL,
                principal=f"User:test",
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
    """
    acl_futures = admin.create_acls(broker_acls)
    # Check ACLs were successfully created
    for future in acl_futures.values():
        future.result()
    admin.poll(0)


if __name__ == "__main__":
    environ[
        "KAFKA_SERVERS"
    ] = "b-1.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096,b-2.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096"
    # "b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196,b-2-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196"
    environ["KAFKA_SECURITY_PROTOCOL"] = "SASL_SSL"
    environ["KAFKA_SASL_MECHANISM"] = "SCRAM-SHA-512"
    environ["KAFKA_SASL_USERNAME"] = "test"
    environ["KAFKA_SASL_PASSWORD"] = "tb6hNQ3P863GaD42U6X2"
    create_acls()
