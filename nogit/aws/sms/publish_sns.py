import boto3
from pprint import pprint
from json import dumps
sso_id = "bac3253f-5040-44ff-a3a0-8f71ac918f00"
sso_user = {
    "attributes":{
        "sso_id": sso_id
    }
}
attributes = {
            "env": {"DataType": "String", "StringValue": "dev"},
            "event": {"DataType": "String", "StringValue": "update-password"},
}
client = boto3.client('sns',region_name="us-west-2")
response = client.publish(
    TopicArn="arn:aws:sns:us-west-2:180477243137:roles-permissions-updater-dev",
    Subject= "example subject",
    Message="example message",
    MessageAttributes=attributes,
)
pprint(response)