from jwt import encode
from time import time
from faker import Faker
faker = Faker()

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
jwtoken = encode(claims,"secret",algorithm="HS256").decode()
print(jwtoken)