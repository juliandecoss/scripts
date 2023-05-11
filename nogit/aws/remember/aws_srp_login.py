""" def get_password_authentication_key(self, username, password, server_b_value, salt):
        u_value = calculate_u(self.large_a_value, server_b_value)
        if u_value == 0:
            raise ValueError('U cannot be zero.')
        username_password = '%s%s:%s' % (self.pool_id, username, password)
        username_password_hash = hash_sha256(username_password.encode('utf-8'))

        x_value = hex_to_long(hex_hash(pad_hex(salt) + username_password_hash))
        g_mod_pow_xn = pow(self.g, x_value, self.big_n)
        int_value2 = server_b_value - self.k * g_mod_pow_xn
        s_value = pow(int_value2, self.small_a_value + u_value * x_value, self.big_n)
        hkdf = compute_hkdf(bytearray.fromhex(pad_hex(s_value)),
                            bytearray.fromhex(pad_hex(long_to_hex(u_value))))
        return hkdf

def process_challenge(self, challenge_parameters):
        user_id_for_srp = challenge_parameters['USERNAME']
        salt_hex = challenge_parameters['SALT']
        srp_b_hex = challenge_parameters['SRP_B']
        secret_block_b64 = challenge_parameters['SECRET_BLOCK']
        # re strips leading zero from a day number (required by AWS Cognito)
        timestamp = re.sub(r" 0(\d) ", r" \1 ",
                           datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y"))
        hkdf = self.get_password_authentication_key(self.device_key,
                                                    self.password, hex_to_long(srp_b_hex), salt_hex)
        secret_block_bytes = base64.standard_b64decode(secret_block_b64)
        msg = bytearray(self.pool_id, 'utf-8') + bytearray(self.device_key, 'utf-8') + \
            bytearray(secret_block_bytes) + bytearray(timestamp, 'utf-8')
        hmac_obj = hmac.new(hkdf, msg, digestmod=hashlib.sha256)
        signature_string = base64.standard_b64encode(hmac_obj.digest())
        response = {
                    'DEVICE_KEY':self.device_key,
                    'TIMESTAMP': timestamp,
                    'USERNAME': user_id_for_srp,
                    'PASSWORD_CLAIM_SECRET_BLOCK': secret_block_b64,
                    'PASSWORD_CLAIM_SIGNATURE': signature_string.decode('utf-8')}
        if self.client_secret is not None:
            response.update({
                "SECRET_HASH":
                self.get_secret_hash(self.username, self.client_id, self.client_secret)})
        return response """
user_pool = 'us-west-2_PqrIVeNNd'
print(user_pool.startswith("us-west"))