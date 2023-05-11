import boto3 
from pprint import pprint
from json import dumps

dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url="http://localhost:8000"
            )
        
table = dynamodb.Table('Schemas')
response = table.scan()

items = response['Items']
with open('/Users/intern/projects/nogit/cognito/dynamo/schemas.txt',"w")as  f:
    f.write(dumps(items))
pprint(items)
