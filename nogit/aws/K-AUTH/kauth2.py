""" TOTP """
import hmac
import time, base64
from MFA_CONSTANTS import MFA_SECRET
from uuid import uuid4

def totp(key: bytes):
    """ Calculate TOTP using time and key """
    now = int(time.time() // 30)
    msg = now.to_bytes(8, "big")
    digest = hmac.digest(key, msg, "sha1")
    offset = digest[19] & 0xF
    code = digest[offset : offset + 4]
    code = int.from_bytes(code, "big") & 0x7FFFFFFF
    code = code % 1000000
    return "{:06d}".format(code)
user = "konfioauth@gmail.com"
#user = "smsprueba@gmail.com"
secret_code = MFA_SECRET[user]
secret_code = "U42OAOPPKYTAMBH7"
key = base64.b32decode(secret_code)

otp = totp(key)
print(otp)
