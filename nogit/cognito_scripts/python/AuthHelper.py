from base64 import standard_b64decode, standard_b64encode
from binascii import hexlify
from hashlib import sha256
from hmac import digest
from os import urandom

from six import string_types


class AuthHelper:
    hex_n = (
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        + "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        + "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        + "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
        + "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
        + "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F"
        + "83655D23DCA3AD961C62F356208552BB9ED529077096966D"
        + "670C354E4ABC9804F1746C08CA18217C32905E462E36CE3B"
        + "E39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9"
        + "DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
        + "15728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64"
        + "ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7"
        + "ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6B"
        + "F12FFA06D98A0864D87602733EC86A64521F2B18177B200C"
        + "BBE117577A615D6C770988C0BAD946E208E24FA074E5AB31"
        + "43DB5BFCE0FD108E4B82D120A93AD2CAFFFFFFFFFFFFFFFF"
    )

    def __init__(self, identifier):
        self.big_n = self.hex_to_big_int(self.hex_n)
        self.big_g = self.hex_to_big_int("2")
        self.big_k = self.hex_to_big_int(
            self.hex_hash(
                f"{self.big_int_to_padded_hex(self.big_n)}{self.big_int_to_padded_hex(self.big_g)}"
            )
        )
        self.small_a = self.get_random_a()
        self.get_big_a()
        self.hex_a = self.big_to_hex(self.big_a)
        self.info_bits = bytearray("Caldera Derived Key", "utf-8")
        self.identifier = identifier

    def hex_to_big_int(self, hex_string):
        return int(hex_string, 16)

    def hash_sha256(self, buf):
        a = sha256(buf).hexdigest()
        return (64 - len(a)) * "0" + a

    def hex_hash(self, hex_string):
        return self.hash_sha256(bytearray.fromhex(hex_string))

    def big_to_hex(self, long_num):
        return "%x" % long_num

    def big_int_to_padded_hex(self, big_int):
        if not isinstance(big_int, string_types):
            hash_str = self.big_to_hex(big_int)
        else:
            hash_str = big_int
        if len(hash_str) % 2 == 1:
            hash_str = "0%s" % hash_str
        elif hash_str[0] in "89ABCDEFabcdef":
            hash_str = "00%s" % hash_str
        return hash_str

    def b64_encode(self, value):
        if hasattr(value, "encode"):
            value = value.encode()
        return standard_b64encode(value).decode()

    def b64_decode(self, value):
        return standard_b64decode(value)

    def get_random_bytes(self, nbytes):
        return hexlify(urandom(nbytes))

    def get_random_big_int(self, nbytes):
        return self.hex_to_big_int(self.get_random_bytes(nbytes))

    def get_random_string(self):
        return self.b64_encode(self.get_random_bytes(40))

    def get_random_a(self):
        random_big_int = self.get_random_big_int(128)
        return random_big_int % self.big_n

    def calculate_big_a(self):
        big_a = pow(self.big_g, self.small_a, self.big_n)
        if (big_a % self.big_n) == 0:
            raise ValueError("Safety check for A failed")
        return big_a

    def get_big_a(self):
        if not hasattr(self, "big_a"):
            self.big_a = self.calculate_big_a()
        return self.big_a

    def get_full_password(self, identifier, identity, password):
        full_password = f"{identifier}{identity}:{password}"
        return self.hash_sha256(full_password.encode())

    def calculate_big_u(self, big_b):
        u_hex_hash = self.hex_hash(
            self.big_int_to_padded_hex(self.big_a) + self.big_int_to_padded_hex(big_b)
        )
        return self.hex_to_big_int(u_hex_hash)

    def calculate_big_x(self, salt_hex, full_password):
        return self.hex_to_big_int(self.hex_hash(salt_hex + full_password))

    def calculate_big_s(self, big_x, big_b, big_u):
        g_mod_pow_xn = pow(self.big_g, big_x, self.big_n)
        int_value_2 = big_b - self.big_k * g_mod_pow_xn
        result = pow(int_value_2, self.small_a + big_u * big_x, self.big_n)
        return result % self.big_n

    def hmac(self, key, msg):
        return digest(key, msg, "sha256")

    def compute_hkdf(self, input_key_material, salt):
        info_bits_update = self.info_bits + bytearray(chr(1), "utf-8")
        prk = self.hmac(salt, input_key_material)
        return self.hmac(prk, info_bits_update)[:16]

    def get_password_authentication_key(self, identity, password, big_b, big_salt):
        if not big_b % self.big_n:
            raise ValueError("B cannot be zero.")

        big_u = self.calculate_big_u(big_b)
        if not big_u:
            raise ValueError("U cannot be zero.")

        full_password = self.get_full_password(self.identifier, identity, password)
        salt_hex = self.big_int_to_padded_hex(big_salt)
        big_x = self.calculate_big_x(salt_hex, full_password)
        big_s = self.calculate_big_s(big_x, big_b, big_u)
        return self.compute_hkdf(
            bytearray.fromhex(self.big_int_to_padded_hex(big_s)),
            bytearray.fromhex(self.big_int_to_padded_hex(big_u)),
        )

    def get_password_claim_signature(
        self, identity, password, big_b, big_salt, secret_block, timestamp
    ):
        hkdf = self.get_password_authentication_key(identity, password, big_b, big_salt)
        msg = (
            bytearray(self.identifier, "utf-8")
            + bytearray(identity, "utf-8")
            + bytearray(self.b64_decode(secret_block))
            + bytearray(timestamp, "utf-8")
        )
        return self.b64_encode(self.hmac(hkdf, msg))

    def generate_device_hashes(self, device_group, device_key):
        device_password = self.get_random_string()
        full_password = self.get_full_password(
            device_group, device_key, device_password
        )
        random_hex = self.get_random_big_int(16)
        salt_to_hash_devices = self.big_int_to_padded_hex(random_hex)
        big_x = self.calculate_big_x(salt_to_hash_devices, full_password)
        big_verifier_devices = pow(self.big_g, big_x, self.big_n)
        verifier_devices_hex = self.big_int_to_padded_hex(big_verifier_devices)
        salt = bytearray.fromhex(salt_to_hash_devices)
        verifier_devices = bytearray.fromhex(verifier_devices_hex)
        return {
            "device_password": device_password,
            "salt": self.b64_encode(salt),
            "verifier_devices": self.b64_encode(verifier_devices),
        }
