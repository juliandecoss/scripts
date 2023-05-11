import json

orignal = {
    "fields": [{"name": "id", "type": "int"}],
    "name": "account_created_key",
    "namespace": "mx.konfio.auth",
    "type": "record",
}
f = open("confluent/template_avro.json")
data = json.load(f)
fields = [{"name": "id", "type": "int"}]
data["name"] = "k-topic-example-api-key"
data["fields"] = fields
schema = json.dumps(data)
schema_or = json.dumps(orignal)
