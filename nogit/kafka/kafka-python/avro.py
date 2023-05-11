import json

with open("account_created_key.avsc", "r") as schema_file:
    schema_str = schema_file.read()
    dict = json.loads(schema_str)
    schema_str_clean = json.dumps(dict)
    print(schema_str_clean)
    print(type(schema_str_clean))
    breakpoint()

with open("account_created_value.avsc", "r") as schema_file:
    schema_str = schema_file.read()
    dict = json.loads(schema_str)
    schema_str_clean = json.dumps(dict)
    print(schema_str_clean)
    print(type(schema_str_clean))
