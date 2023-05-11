import json
from pprint import pprint

from confluent_kafka.schema_registry import Schema, SchemaRegistryClient

SR_ENDPOINT = "https://psrc-o2wjx.us-east-2.aws.confluent.cloud"
KEY = "HB3XWPZ5PDFD2QHJ"
SECRET = "719hjLbfUlDP+a/Vir4wWJUFHyODYso/MSHSv6OTW6aU3895ZQVj7sog0RtCzVkh"
schema_registry_config = {"url": SR_ENDPOINT, "basic.auth.user.info": f"{KEY}:{SECRET}"}
print(schema_registry_config)
breakpoint()
schema_registry_client = SchemaRegistryClient(schema_registry_config)
# schema = schema_registry_client.get_schema("100016")
# pprint(schema.schema_str)
# schema = schema_registry_client.get_version(f"k-auth-account-created-value", "1")
# pprint(schema.schema.schema_str)

f = open("confluent/template_avro.json")
data = json.load(f)
fields = [
    {"name": "user_id", "type": "int"},
    {"name": "natural_person_id", "type": "int"},
    {"name": "enterprise_id", "type": "int"},
    {"name": "source", "type": "string"},
    {"name": "domain", "type": "string"},
    {"name": "stage", "type": "string"},
    {"name": "screen", "type": "string"},
    {"name": "action", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "phone", "type": "string"},
    {"name": "first_name", "type": "string"},
    {"name": "last_name", "type": "string"},
    {"name": "last_name1", "type": "string"},
    {"name": "last_name2", "type": "string"},
    {"name": "enterprise_customer_type", "type": "string"},
    {"name": "utm_source", "type": "string"},
    {"name": "utm_medium", "type": "string"},
    {"name": "utm_campaign", "type": "string"},
    {"name": "utm_term", "type": "string"},
    {"name": "utm_content", "type": "string"},
]
data["name"] = "k_topic_example_api_value"
data["fields"] = fields
schema_str = json.dumps(data)
print(schema_str)
schema = Schema(schema_str, "AVRO")
response = schema_registry_client.register_schema("k-topic-example-api-value", schema)
pprint(response)
breakpoint()
