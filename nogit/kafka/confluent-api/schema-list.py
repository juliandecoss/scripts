from csv import writer
from json import loads,dumps
from requests import get
from pprint import pprint

SCHEMA_TOKEN = "M0Y0Rkw0NkxGQ1ZLSTRWQTpLSVdzZzdNbzQ5TG1PbkFFcCtzNFJUL3BBejh4bVlKWStIZmFvSjRHTVFqSlFpeXdwazRsdnZrVVRQZGpjR2tK"
SCHEMA_URL = "https://psrc-o2wjx.us-east-2.aws.confluent.cloud/schemas"

#API PARA SCHEMAS
headers = { 'Authorization': f"Basic {SCHEMA_TOKEN}" }
response  = get(SCHEMA_URL,headers=headers)
schemas = response.json()

with open("./nogit/kafka/confluent-api/schemas_list.csv", "w") as schemas_list_file:
    schemas_list_writer = writer(schemas_list_file, delimiter=",")
    schemas_list_writer.writerow(
            [
            "schema_name",
            "schema_name_2",
            "fields",
            "version",
            "tribe",
            "schema_confluent_id",
            ]
        )
    for schema in schemas:
        schema_to_row = []
        schema_data = loads(schema['schema'])
        schema_to_row.append(schema['subject'])
        schema_to_row.append(schema_data['name'])
        schema_to_row.append(dumps(schema_data['fields']))
        print(type(schema_data['fields']))  
        schema_to_row.append(schema['version'])
        schema_to_row.append("undefined")
        schema_to_row.append(schema['id'])
        schemas_list_writer.writerow(schema_to_row)
