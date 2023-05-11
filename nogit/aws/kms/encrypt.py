from boto3 import client
from pprint import pprint
from base64 import b64encode,b64decode,encodebytes
from base64 import b32encode
client = client('kms')
sso_key = "alias/dev/platform/sso"
response = client.encrypt(
    KeyId="alias/konfio/secrets",
    Plaintext="us-west-2_9CGG2sPam".encode(),
)
#pprint(response)
print(response['CiphertextBlob'])
print(type(response['CiphertextBlob']))
print(b32encode(response['CiphertextBlob']))
print(b32encode(response['CiphertextBlob']).decode())


response2 = client.decrypt(
    CiphertextBlob=response['CiphertextBlob'],
    KeyId="alias/konfio/secrets",
)
pprint(response2)

