import base64
import hashlib
import hmac

import boto3
from faker import Faker

faker = Faker()
Faker.seed(1)
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

create_account = client.sign_up(
    ClientId=client_id,
    SecretHash=secret_hash,
    Username=user,
    Password=password,
    UserAttributes=[
        {"Name": "phone_number", "Value": phone},
        {"Name": "name", "Value": faker.first_name()},
        {"Name": "custom:paternal_last_name", "Value": faker.last_name_male()},
        {"Name": "custom:maternal_last_name", "Value": faker.last_name_female()},
        {"Name": "email", "Value": user},
    ],
)
