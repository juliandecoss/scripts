from requests import get
from pprint import pprint

SCHEMA_TOKEN = "M0Y0Rkw0NkxGQ1ZLSTRWQTpLSVdzZzdNbzQ5TG1PbkFFcCtzNFJUL3BBejh4bVlKWStIZmFvSjRHTVFqSlFpeXdwazRsdnZrVVRQZGpjR2tK"
id = '100015'
schema_url = f"https://psrc-o2wjx.us-east-2.aws.confluent.cloud/schemas/ids/{id}/schema"
headers = { 'Authorization': f"Basic {SCHEMA_TOKEN}" }
response  = get(schema_url,headers=headers)
schemas = response.json()
fields =  schemas['fields']
print(type(fields))
pprint(fields)
