from csv import writer
from requests import get
import boto3
from datetime import datetime
from pprint import pprint
from csv import reader
from json import dumps

SCHEMA_TOKEN = "M0Y0Rkw0NkxGQ1ZLSTRWQTpLSVdzZzdNbzQ5TG1PbkFFcCtzNFJUL3BBejh4bVlKWStIZmFvSjRHTVFqSlFpeXdwazRsdnZrVVRQZGpjR2tK"
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Schemas')
max_fields = 31

def get_schema(schema_id):
    schema_url = f"https://psrc-o2wjx.us-east-2.aws.confluent.cloud/schemas/ids/{schema_id}/schema"
    headers = { 'Authorization': f"Basic {SCHEMA_TOKEN}" }
    response  = get(schema_url,headers=headers)
    schemas = response.json()
    return schemas['fields']

with open("/Users/intern/projects/nogit/cognito/dynamo/schemas.csv") as schemas_list_file:
    schemas_list_reader = reader(schemas_list_file)
    for pos,schema in enumerate(schemas_list_reader):
        if pos > 0:
            name = schema[0]
            creation_date = schema[5]
            tribe = schema[3]
            version = schema[2]
            schema_id = schema[4]
            fields = get_schema(schema_id)
            item = {
                'CreationDate': creation_date,
                'Tribe': tribe,
                'Version': version,
                'Fields': fields,
                'SchemaConfluentId': schema_id,
                'Name': name,
            }
            insert_item_resp = table.put_item(
                Item=item
            )

# 'k-mining-cfdi-invoice-data-value' 32
#  'k-payments-liquidation-approved-transactions-value' 5486 2
