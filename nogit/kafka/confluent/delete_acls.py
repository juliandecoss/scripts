from os import environ
from pprint import pprint
from socket import gethostname

from confluent_kafka.admin import (AclBindingFilter, AclOperation,
                                   AclPermissionType, AdminClient,
                                   ResourcePatternType, ResourceType)


def logger(action, msg):
    print("*" * 10, f"{action}:\n", msg)


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


def delete_acls():
    # Check ACL exists
    admin = create_admin_client()
    acl_filter = AclBindingFilter(
        restype=ResourceType.ANY,
        name=None,
        resource_pattern_type=ResourcePatternType.ANY,
        principal=None,
        host=None,
        operation=AclOperation.ANY,
        permission_type=AclPermissionType.ANY,
    )
    acls_future = admin.delete_acls(acl_binding_filters=acl_filter)
    pprint(acls_future)


if __name__ == "__main__":
    environ[
        "KAFKA_SERVERS"
    ] = "b-1.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096,b-2.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096"
    # "b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196,b-2-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196"
    environ["KAFKA_SECURITY_PROTOCOL"] = "SASL_SSL"
    environ["KAFKA_SASL_MECHANISM"] = "SCRAM-SHA-512"
    environ["KAFKA_SASL_USERNAME"] = "test"
    environ["KAFKA_SASL_PASSWORD"] = "tb6hNQ3P863GaD42U6X2"
    delete_acls()
