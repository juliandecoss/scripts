import datetime
from json import dumps, loads
from typing import Callable

from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from events import generate_event

topic = "k-topic-example-api"
SR_ENDPOINT = "https://psrc-o2wjx.us-east-2.aws.confluent.cloud"
KEY = "HB3XWPZ5PDFD2QHJ"
SECRET = "719hjLbfUlDP+a/Vir4wWJUFHyODYso/MSHSv6OTW6aU3895ZQVj7sog0RtCzVkh"
version = "1"
type = "key"
producer_config = {
    "bootstrap.servers": "pkc-pgq85.us-west-2.aws.confluent.cloud:9092",  # pkc-pgq85.us-west-2.aws.confluent.cloud:9092
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "2BTAQMWETOMDBYW7",  # ZVNIM6R2F4MLWR7E
    "sasl.password": "wERz2XSgWASkF267z+7wwcooKO+qy9EI2TMANH75kh7lHwI0lu2OZ/0x6hydOfea",  # LzyaQZO2/LsluUR2pmSdABlbWeyO4xLxdgb3+pSjwYSAZRe+WRnL5af6jr/L/EwR
    #"session.timeout.ms": "45000",  # 45000
}


class obj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    return loads(dumps(dict1), object_hook=obj)

def objectify(dict1: dict) -> obj:
    return loads(dumps(dict1), object_hook=obj)

def get_schema_serializer(
    type: str = "key",
    topic: str = "",
    version: str = "1",
    serialize_func: Callable = None,
) -> AvroSerializer:

    schema_registry_config = {
        "url": SR_ENDPOINT,
        "basic.auth.user.info": f"{KEY}:{SECRET}",
    }
    schema_registry_client = SchemaRegistryClient(schema_registry_config)
    schema = schema_registry_client.get_version(f"{topic}-{type}", version)
    avro_serializer = AvroSerializer(
        schema_registry_client=schema_registry_client,
        schema_str=schema.schema.schema_str,
        to_dict=serialize_func,
        conf={"auto.register.schemas": False},
    )
    avro_serializer._schema_id = schema.schema_id
    avro_serializer._schema_name = schema.subject
    return avro_serializer


def get_serializing_producer(
    key_schema: AvroSerializer, value_schema: AvroSerializer
) -> SerializingProducer:
    return SerializingProducer(
        {
            **producer_config,
            "key.serializer": key_schema,
            "value.serializer": value_schema,
        }
    )

for i in range (10):
    dictionary = generate_event()
    dictionary['user_id'] = i
    vobj = objectify(dictionary)
    value_obj = dict2obj(dictionary)
    key_obj = dict2obj({"id": value_obj.user_id})
    key_avro_serializer = get_schema_serializer(
        "key", topic, "1", lambda trace_key_obj, ctx: trace_key_obj.__dict__
    )

    value_avro_serializer = get_schema_serializer(
        "value", topic, "1", lambda trace_obj, ctx: trace_obj.__dict__
    )
    producer = get_serializing_producer(key_avro_serializer, value_avro_serializer)
    try:
        producer.produce(
            topic=topic,
            key=key_obj,
            value=value_obj,
            headers=[
                ("event_name", "account_created"),
            ],
        )
        producer.poll(0)
        producer.flush()
    except Exception as e:
        e.args
        print(f"Error {e}")
    print(f"Successful message sent {i} user_id: {value_obj.user_id}")
    #breakpoint()
