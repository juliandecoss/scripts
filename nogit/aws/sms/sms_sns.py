import boto3
from pprint import pprint
client = boto3.client('sns')

response = client.publish(
    PhoneNumber='+12127290149',
    Message='Konfio te envía un SMS con número 123456',
)
pprint(response)