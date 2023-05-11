from time import time_ns

import argparse
import os

from confluent_kafka import Consumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import MessageField, SerializationContext
from json import loads,dumps

SR_ENDPOINT = "https://psrc-o2wjx.us-east-2.aws.confluent.cloud"
KEY = "HB3XWPZ5PDFD2QHJ"
SECRET = "719hjLbfUlDP+a/Vir4wWJUFHyODYso/MSHSv6OTW6aU3895ZQVj7sog0RtCzVkh"

class User(object):
    """
    User record
    Args:
        name (str): User's name
        favorite_number (int): User's favorite number
        favorite_color (str): User's favorite color
    """

    def __init__(self, name=None, favorite_number=None, favorite_color=None):
        self.name = name
        self.favorite_number = favorite_number
        self.favorite_color = favorite_color


def dict_to_user(obj, ctx):
    """
    Converts object literal(dict) to a User instance.
    Args:
        obj (dict): Object literal(dict)
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    """

    if obj is None:
        return None

    return User(
        name=obj["name"],
        favorite_number=obj["favorite_number"],
        favorite_color=obj["favorite_color"],
    )

class obj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)

def get_time(start_time):
    return (time_ns() - start_time) // 1000000 if start_time > 0 else None

def dict2obj(dict1,ctx):
    return loads(dumps(dict1), object_hook=obj)

def main():
    inital_time = time_ns()
    not_touched_initial_time = time_ns()
    topic = "k-topic-example-api"
    
    # path = os.path.realpath(os.path.dirname(__file__))
    # with open(f"{path}/avro/schema") as f:
    #     schema_str = f.read() 

    schema_registry_config = {
        "url": SR_ENDPOINT,
        "basic.auth.user.info": f"{KEY}:{SECRET}",
    }
    schema_registry_client = SchemaRegistryClient(schema_registry_config)
    type = "value"
    value_schema = schema_registry_client.get_version(f"{topic}-{type}", "1")
    key_schema = schema_registry_client.get_version(f"{topic}-key", "1")
    value_avro_deserializer = AvroDeserializer(
        schema_registry_client, value_schema.schema.schema_str, dict2obj
    )
    key_avro_deserializer = AvroDeserializer(
        schema_registry_client, key_schema.schema.schema_str, dict2obj
    )

    consumer_conf = {
        "bootstrap.servers": "pkc-pgq85.us-west-2.aws.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "HMNHCMAFBFLBBHFH",
        "sasl.password": "liGWoy7pAlcHQPKRVufB1txXn/BcOTBG2Bz04mjyv47zGayLZoVKs8VYpdv7Rfcy",
        "group.id": "simple loop1",#"group"
        "auto.offset.reset": "earliest",
        "debug":"broker"
    }
    MIN_COMMIT_COUNT = 1
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])
    attempts = 0
    msg_count = 0
    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                attempts += 1
                print(attempts)
                if attempts == 10:
                    break
                continue

            user_values = value_avro_deserializer(
                msg.value(), SerializationContext(msg.topic(), MessageField.VALUE)
            )
            user_keys = key_avro_deserializer(
                msg.key(), SerializationContext(msg.topic(), MessageField.KEY)
            )
            if user_values is not None:
                #breakpoint()
                #consumer.commit(asynchronous=True)
                attempts = 0
                final_time = get_time(inital_time)
                inital_time = time_ns()
                print(f"Tiempo que tomo consumir: {final_time}")
                # print(f"Topic {msg.topic()}")
                print(f"Key: {user_keys.id}")
                print(f"Offset message {msg.offset()}")
                print(f"Partition {msg.partition()}")
                print(f"#############################")
                #print(f"Headers {msg.headers()[0]}")
                #print(f"Values: email={user_values.email}, natural_person_id={user_values.natural_person_id}")
                msg_count += 1
                # if msg_count % MIN_COMMIT_COUNT == 0:
        except KeyboardInterrupt:
            break
    print(f"Total time is :{get_time(not_touched_initial_time)}")
    consumer.close()


if __name__ == "__main__":
    
    main()
