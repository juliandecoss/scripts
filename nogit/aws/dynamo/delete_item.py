import boto3
client = boto3.client('dynamodb',endpoint_url="http://localhost:8000",
                region_name = 'us-west-2',
                aws_access_key_id="RANDOM",
                aws_secret_access_key="RANDOM",)
response = client.delete_item(
    TableName='Schemas',
    Key={
        'Name': 'k-payments-dispersed-transactions-value'
    },
)