import boto3
from pprint import pprint
from json import dumps

dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url="http://localhost:8000",
                region_name = 'us-west-2',
                aws_access_key_id="RANDOM",
                aws_secret_access_key="RANDOM",
            )
        
table = dynamodb.Table('InventoryRoyalHolidayTest')
response = table.scan()

items = response['Items']
pprint(items)
