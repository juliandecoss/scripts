import boto3


dynamodb = boto3.resource(
                            'dynamodb',
                            endpoint_url="http://localhost:8000"
                        )

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Schemas',
    KeySchema=[
        {
            'AttributeName': 'SchemaConfluentId',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'CreationDate',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'SchemaConfluentId',
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