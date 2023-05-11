import base64
import binascii
import datetime
import hashlib
import hmac
import re

import boto3
import os
import six

#from exceptions import ForceChangePasswordException

n_hex = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1" \
    + "29024E088A67CC74020BBEA63B139B22514A08798E3404DD" \
    + "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245" \
    + "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED" \
    + "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D" \
    + "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F" \
    + "83655D23DCA3AD961C62F356208552BB9ED529077096966D" \
    + "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B" \
    + "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9" \
    + "DE2BCBF6955817183995497CEA956AE515D2261898FA0510" \
    + "15728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64" \
    + "ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7" \
    + "ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6B" \
    + "F12FFA06D98A0864D87602733EC86A64521F2B18177B200C" \
    + "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB31" \
    + "43DB5BFCE0FD108E4B82D120A93AD2CAFFFFFFFFFFFFFFFF"
g_hex = "2"
info_bits = bytearray("Caldera Derived Key", "utf-8")

def hash_sha256(buf):
    a = hashlib.sha256(buf).hexdigest()
    print(a)
    return (64 - len(a)) * "0" + a

def hex_hash(hex_string):
    return hash_sha256(bytearray.fromhex(hex_string))

def hex_to_long(hex_string):
    return int(hex_string, 16)

def long_to_hex(long_num):
    return "%x" % long_num

def get_random(nbytes):
    random_hex = binascii.hexlify(os.urandom(nbytes))
    return hex_to_long(random_hex)

def pad_hex(long_int):
    if not isinstance(long_int, six.string_types):
        hash_str = long_to_hex(long_int)
    else:
        hash_str = long_int
    if len(hash_str) % 2 == 1:
        hash_str = "0%s" % hash_str
    elif hash_str[0] in "89ABCDEFabcdef":
        hash_str = "00%s" % hash_str
    return hash_str

def compute_hkdf(ikm, salt):
    """
    Standard hkdf algorithm
    :param {Buffer} ikm Input key material.
    :param {Buffer} salt Salt value.
    :return {Buffer} Strong key material.
    @private
    """
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    info_bits_update = info_bits + bytearray(chr(1), 'utf-8')
    hmac_hash = hmac.new(prk, info_bits_update, hashlib.sha256).digest()
    return hmac_hash[:16]


def calculate_u(big_a, big_b):
    """
    Calculate the client's value U which is the hash of A and B
    :param {Long integer} big_a Large A value.
    :param {Long integer} big_b Server B value.
    :return {Long integer} Computed U value.
    """
    u_hex_hash = hex_hash(pad_hex(big_a) + pad_hex(big_b))
    return hex_to_long(u_hex_hash)


def generate_hash_device(device_group_key, device_key):
    
    device_password = base64.standard_b64encode(os.urandom(40)).decode("utf-8")

    combined_string = "%s%s:%s" % (device_group_key, device_key, device_password)
    combined_string_hash = hash_sha256(combined_string.encode("utf-8"))
    print("Combined String Hash: " + combined_string_hash)
    salt = pad_hex(get_random(16))

    x_value = hex_to_long(hex_hash(salt + combined_string_hash))
    g = hex_to_long(g_hex)
    big_n = hex_to_long(n_hex)
    verifier_device_not_padded = pow(g, x_value, big_n)
    verifier = pad_hex(verifier_device_not_padded)

    password_verifier = base64.standard_b64encode(bytearray.fromhex(verifier)).decode("utf-8")
    salt = base64.standard_b64encode(bytearray.fromhex(salt)).decode("utf-8")
    print("PasswordVerifier: " + password_verifier)
    print("Salt: " + salt)
    
    device_secret_verifier_config = {
        "PasswordVerifier": password_verifier,
        "Salt": salt
    }

    return device_password, device_secret_verifier_config

class UserAWS(object):
    NEW_PASSWORD_REQUIRED_CHALLENGE = "NEW_PASSWORD_REQUIRED"
    PASSWORD_VERIFIER_CHALLENGE = "PASSWORD_VERIFIER"

    def __init__(self, username, password, pool_id, client_id, device_key="", pool_region=None, client=None, client_secret=None):
        if pool_region is not None and client is not None:
            raise ValueError("pool_region and client should not both be specified")
        
        self.username = username
        self.password = password
        self.pool_id = pool_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.client = client if client else boto3.client("cognito-idp", region_name=pool_region)
        self.big_n = hex_to_long(n_hex)
        self.g = hex_to_long(g_hex)
        self.k = hex_to_long(hex_hash('00' + n_hex + '0' + g_hex))
        self.small_a_value = self.generate_random_small_a()
        self.large_a_value = self.calculate_a()
        self.srp_a = long_to_hex(self.large_a_value)
        self.device_key = device_key

    def generate_random_small_a(self):
        random_long_int = get_random(128)
        return random_long_int % self.big_n
        
    def calculate_a(self):
        big_a = pow(self.g, self.small_a_value, self.big_n)
        if (big_a % self.big_n) == 0:
            raise ValueError('Safety check for A failed')
        return big_a

    def get_password_authentication_key(self, username, password, server_b_value, salt):
        u_value = calculate_u(self.large_a_value, server_b_value)
        if u_value == 0:
            raise ValueError('U cannot be zero.')
        user_pool_id = self.pool_id
        if user_pool_id.startswith("us-west"):
            user_pool_id = user_pool_id.split("_")[1]
        username_password = '%s%s:%s' % (user_pool_id, username, password)
        username_password_hash = hash_sha256(username_password.encode('utf-8'))

        x_value = hex_to_long(hex_hash(pad_hex(salt) + username_password_hash))
        g_mod_pow_xn = pow(self.g, x_value, self.big_n)
        int_value2 = server_b_value - self.k * g_mod_pow_xn
        s_value = pow(int_value2, self.small_a_value + u_value * x_value, self.big_n)
        hkdf = compute_hkdf(bytearray.fromhex(pad_hex(s_value)),
                            bytearray.fromhex(pad_hex(long_to_hex(u_value))))
        return hkdf

    def get_auth_params(self):
        auth_params = { "USERNAME": self.username, "SRP_A": long_to_hex(self.large_a_value) }
        if self.client_secret is not None:
            auth_params.update({
                "SECRET_HASH": self.get_secret_hash(self.username, self.client_id, self.client_secret)
            })
        return auth_params

    @staticmethod
    def get_secret_hash(username, client_id, client_secret):
        message = bytearray(username + client_id, "utf-8")
        hmac_obj = hmac.new(bytearray(client_secret, 'utf-8'), message, hashlib.sha256)
        return base64.standard_b64encode(hmac_obj.digest()).decode('utf-8')

    def process_challenge(self, challenge_parameters):
        user_id_for_srp = username = challenge_parameters['USERNAME']
        if self.device_key:
            username = self.device_key
        salt_hex = challenge_parameters['SALT']
        srp_b_hex = challenge_parameters['SRP_B']
        secret_block_b64 = challenge_parameters['SECRET_BLOCK']
        # re strips leading zero from a day number (required by AWS Cognito)
        user_pool_id = self.pool_id
        if user_pool_id.startswith("us-west"):
            user_pool_id = user_pool_id.split("_")[1]
        timestamp = re.sub(r" 0(\d) ", r" \1 ",
                           datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y"))
        hkdf = self.get_password_authentication_key(username,
                                                    self.password, hex_to_long(srp_b_hex), salt_hex)
        secret_block_bytes = base64.standard_b64decode(secret_block_b64)
        msg = bytearray(user_pool_id, 'utf-8') + bytearray(username, 'utf-8') + \
            bytearray(secret_block_bytes) + bytearray(timestamp, 'utf-8')
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        signature_string = base64.standard_b64encode(hmac_obj.digest())
        response = {
                    'TIMESTAMP': timestamp,
                    'USERNAME': user_id_for_srp,
                    'PASSWORD_CLAIM_SECRET_BLOCK': secret_block_b64,
                    'PASSWORD_CLAIM_SIGNATURE': signature_string.decode('utf-8')}
        if self.device_key:
            response.update({'DEVICE_KEY':self.device_key})
        if self.client_secret is not None:
            response.update({
                "SECRET_HASH":
                self.get_secret_hash(self.username, self.client_id, self.client_secret)})
        return response

    def authenticate_user(self, client=None):
        boto_client = self.client or client
        auth_params = self.get_auth_params()
        response = boto_client.initiate_auth(
            AuthFlow="USER_SRP_AUTH",
            AuthParameters=auth_params,
            ClientId=self.client_id
        )
        if response["ChallengeName"] == self.PASSWORD_VERIFIER_CHALLENGE:
            challenge_response = self.process_challenge(response['ChallengeParameters'])
            tokens = boto_client.respond_to_auth_challenge(
                ClientId=self.client_id,
                ChallengeName=self.PASSWORD_VERIFIER_CHALLENGE,
                ChallengeResponses=challenge_response)
            if tokens.get('ChallengeName') == self.NEW_PASSWORD_REQUIRED_CHALLENGE:
                raise Exception
            return tokens
        else:
            raise NotImplementedError('The %s challenge is not supported' % response['ChallengeName'])

    def set_new_password_challenge(self, new_password, client=None):
        boto_client = self.client or client
        auth_params = self.get_auth_params()
        response = boto_client.initiate_auth(
            AuthFlow='USER_SRP_AUTH',
            AuthParameters=auth_params,
            ClientId=self.client_id
        )
        if response['ChallengeName'] == self.PASSWORD_VERIFIER_CHALLENGE:
            challenge_response = self.process_challenge(response['ChallengeParameters'])
            tokens = boto_client.respond_to_auth_challenge(
                ClientId=self.client_id,
                ChallengeName=self.PASSWORD_VERIFIER_CHALLENGE,
                ChallengeResponses=challenge_response)

            if tokens['ChallengeName'] == self.NEW_PASSWORD_REQUIRED_CHALLENGE:
                challenge_response = {
                    'USERNAME': auth_params['USERNAME'],
                    'NEW_PASSWORD': new_password
                }
                new_password_response = boto_client.respond_to_auth_challenge(
                    ClientId=self.client_id,
                    ChallengeName=self.NEW_PASSWORD_REQUIRED_CHALLENGE,
                    Session=tokens['Session'],
                    ChallengeResponses=challenge_response)
                return new_password_response
            return tokens
        else:
            raise NotImplementedError('The %s challenge is not supported' % response['ChallengeName'])