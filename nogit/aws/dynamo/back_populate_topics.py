import boto3
from csv import reader

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Topics')

with open("/Users/intern/projects/nogit/cognito/dynamo/topics.csv") as topics_list_file:
    topics_list_reader = reader(topics_list_file)
    for pos,topic in enumerate(topics_list_reader):
        if pos > 0:
            print(topic)
            insert_item_resp = table.put_item(
                Item={
                    'Name': topic[0],
                    'Tribe':topic[1],
                    'CreationDate':topic[2],
                }
            )
    