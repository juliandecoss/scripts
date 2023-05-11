import boto3
from datetime import datetime

dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url="http://localhost:8000"
            )

table = dynamodb.Table('Schemas')

insert_item_resp = table.put_item(
    Item={
        'SchemaConfluentId': "10002",
        'Name': "k-confluent-api-alv2",
        'Fields': [{"name":"np_id","type":"int"}],
        'Version': "2",
        'Owner': "alonso1.juarez@konfio.mx",
        'Squad':"Platform-Services",
        'Tribe':'Platform-Foundations',
        'CreationDate':str(datetime.now()).split(".")[0],
    }
)

print(insert_item_resp)