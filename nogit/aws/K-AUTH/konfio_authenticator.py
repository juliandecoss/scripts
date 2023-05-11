import hmac, base64, struct, hashlib, time
import six
import re

def get_hotp(secret,intervals_no,as_string=False,casefold=False,digest_method=hashlib.sha1,token_length=6):
    if isinstance(secret, six.string_types):
        # It is unicode, convert it to bytes
        secret = secret.encode('utf-8')
    # Get rid of all the spacing:
    secret = secret.replace(b' ', b'')
    try:
        key = base64.b32decode(secret, casefold=casefold)
    except (TypeError):
        raise TypeError('Incorrect secret')
    msg = struct.pack('>Q', intervals_no)
    hmac_digest = hmac.new(key, msg, digest_method).digest()
    ob = hmac_digest[19] if six.PY3 else ord(hmac_digest[19])
    o = ob & 15
    token_base = struct.unpack('>I', hmac_digest[o:o + 4])[0] & 0x7fffffff
    token = token_base % (10 ** token_length)
    if as_string:
        # TODO: should as_string=True return unicode, not bytes?
        return six.b('{{:0{}d}}'.format(token_length).format(token))
    else:
        return token


def get_totp(
        secret,
        as_string=False,
        digest_method=hashlib.sha1,
        token_length=6,
        interval_length=30,
        clock=None,
):
    if clock is None:
        clock = time.time()
    interv_no = int(clock) // interval_length
    return get_hotp(
        secret,
        intervals_no=interv_no,
        as_string=as_string,
        digest_method=digest_method,
        token_length=token_length,
    )
user = "konfioauth@gmail.com"
secret = f"otpauth://totp/{user}?secret=CEVCG6LJKM3QSOXJDRUQTEKBMUEUAQILNW3RLYMBQKLU2WQXWOIA"
secret_code = "CEVCG6LJKM3QSOXJDRUQTEKBMUEUAQILNW3RLYMBQKLU2WQXWOIA===="
OTP = get_totp(secret_code)
print(OTP)
