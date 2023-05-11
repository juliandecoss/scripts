import boto3
from constants import REFRESH_TOKEN
from datetime import datetime
#client = boto3.client('s3')
client = boto3.client('s3', region_name = 'us-west-2')
response = client.put_object(
    Body=REFRESH_TOKEN.encode(),
    Bucket='entity-documents-local',
    ContentLength=123,
    Key='pruebaparacore',
)
#Expires=datetime(2021, 9, 3, 11),
#ServerSideEncryption='AES256'|'aws:kms',
#SSECustomerKey='string',
#SSEKMSKeyId='string',
#BucketKeyEnabled=True|False,
#arn:aws:s3:us-west-2:180477243137:accesspoint/entity-documents-dev/miprimerrefresh_token1
