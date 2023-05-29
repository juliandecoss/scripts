import boto3


dynamodb = boto3.resource(
                    'dynamodb',
                    endpoint_url="http://localhost:8000",
                    region_name = 'us-west-2',
                    aws_access_key_id="RANDOM",
                    aws_secret_access_key="RANDOM",
)

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='InventoryRoyalHolidayTest',
    KeySchema=[
        {
            'AttributeName': 'RoomId',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'CreationDate',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'RoomId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'CreationDate',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)