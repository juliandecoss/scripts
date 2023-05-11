from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from jwt import encode, decode
from time import time
from faker import Faker
from  pprint import pprint
faker = Faker()

def generate_key_pairs():
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )

    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption()
    )

    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    return private_key, public_key
private_key, public_key =generate_key_pairs()
def mock_token():
    claims={
        "sub": faker.uuid4(),
        "token_use": "access",
        "scope": faker.url(),
        "auth_time": int(time()),
        "iss": faker.url(),
        "exp": int(time() + 600),
        "iat": int(time()),
        "version": 2,
        "jti": faker.uuid4(),
        "client_id": faker.uuid4(),
    }
    return encode(claims, private_key, algorithm="RS256")
token = mock_token()
print(token)
pprint(decode(token, public_key, algorithms=["RS256"]))