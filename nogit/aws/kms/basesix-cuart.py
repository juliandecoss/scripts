from base64 import b64encode
from faker import Faker

faker = Faker()
kms_response = {"CiphertextBlob": faker.sha256().encode()}
h = b64encode(kms_response["CiphertextBlob"]).decode()
print(h)