import base64
import hashlib
import hmac
import json
import sys

import boto3

client = boto3.client("cognito-idp", region_name="us-west-2")

user_pool = "us-west-2_PqrIVeNNd"
client_id = "2v3tko99u3eiid4hie80udvclk"
client_secret = "mj8m1qlsmm639cu0an7rqa1a0bkpmch05u6g435c6m67v8mh28i"
user = "elpaip@gmail.com"
password = "Tests@123"
phone = "+525549490369"

message = bytes(user + client_id, "utf-8")
key = bytes(client_secret, "utf-8")
secret_hash = base64.b64encode(
    hmac.new(key, message, digestmod=hashlib.sha256).digest()
).decode()

response = client.verify_software_token(
    AccessToken=sys.argv[1], UserCode=sys.argv[2], FriendlyDeviceName="Rofl"
)

print(json.dumps(response, sort_keys=True, indent=4))
