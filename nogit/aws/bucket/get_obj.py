import boto3
from pprint import pprint

def get_s3_object(bucket: str, key_path: str) -> dict:
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket=bucket, Key=key_path)
    response["Body"] = response["Body"].read()
    return response

datos = get_s3_object("entity-documents-dev","natural-person-req-docs/1492990/sso/refresh_tokens/682712")
pprint(datos["Body"].decode())