from time import time

from faker import Faker
from jose.jwk import construct
from jose.jwt import encode
from pprint import pprint
faker = Faker()


def get_public_key(kid=None, alg=None):
    key = {"kid": kid or faker.sha1(), "alg": alg or "RS256", "use": "sig"}
    signature = {}
    alg_is = lambda x: key["alg"].startswith(x)
    if alg_is("RS"):
        signature = {
            "kty": "RSA",
            "e": "AQAB",
            "n": "thBvC_I9NciW6XqTxUFMZaVVpvGx6BvLHd3v8Visk_6OoDCVXF_6vNktNi6W7CBkuHBqGyuF0wDFrHcZuZq_kLKI6IRofEzKyUoReOyYRlPt5ar64oDO-4mwH47fb99ILW94_8RpQHy74hCnfv7d888YaCmta9iOBOvggcvxb5s",
            "d": "RSjC9hfDtq2G3hQJFBI08hu3CJ6hRRlhs-u9nMFhdSpqhWFPK3LuLVSWPxG9lN7NQ963_7AturR9YoEvjXjCMZFEEqewNQNq31v0zgh9k5XFdz1CiVSLdHo7VQjuJB6imLCF266TUFvZwQ4Gs1uq6I6GCVRoenSe9ZsWleYF--E",
        }
    elif alg_is("HS"):
        signature = {"kty": "oct", "k": faker.sha1()}
    key.update(signature)
    return key


def generate_private_key(kid=None, alg=None):
    key = get_public_key(kid, alg)
    return construct(key).to_dict()

pprint(generate_private_key())