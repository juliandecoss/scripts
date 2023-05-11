from boto3 import client
from pprint import pprint
from base64 import b64encode,b64decode,encodebytes
from json import dumps, loads
from redis import Redis

client = client('kms')
identity = "sms@gmail.com"
credential = "Tests@123"
credentials = {"identity":identity,"credential":credential}
pariba = dumps(credentials)

response = client.encrypt(
    KeyId="alias/dev/platform/sso",
    Plaintext=pariba.encode(),
)
paredis = b64encode(response['CiphertextBlob']).decode()
redis_vars = {"port": "6379", "host": 'localhost'}
r = Redis(**redis_vars)
r.set("hola",paredis,100000)
fromredis = r.get("hola")
response2 = client.decrypt(
    CiphertextBlob=b64decode(fromredis),
    KeyId="alias/dev/platform/sso",
)
print(response2['Plaintext'])
user_data = loads(response2['Plaintext'].decode())
print(user_data["credential"])