import boto3
import hmac, hashlib, base64
from pprint import pprint

client = boto3.client('cognito-idp', region_name = 'us-west-2')
user_pool = 'us-west-2_SGHXfzcyN'
client_id = '137ff7lhsd5dvs7odetc1jdq6k'
client_secret = '114gkjkp3ooug5hdl198havs95l1d7quafultapcba3g61t4v3rq'
user='konfioauth@gmail.com'
password='Tests@123'
phone='+529611230729'

def create_hash(user, client_id, client_secret):
    message = bytes(user+client_id,'utf-8')
    key = bytes(client_secret,'utf-8')
    secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
    return secret_hash
create_account= client.sign_up(
    ClientId=client_id,
    SecretHash=create_hash(user,client_id,client_secret),
    Username=user,
    Password=password,
    UserAttributes=[
        {
            "Name":"phone_number",
            "Value": phone,
        },
        {
            "Name":"name",
            "Value": "Prueba",
        },
        {
            "Name":"custom:paternal_last_name",
            "Value": "Para MFA y Device",
        },
        {
            "Name":"custom:maternal_last_name",
            "Value": "Longevo",
        },
        {
            "Name":"email",
            "Value":user,
        },
    ]
)
pprint(create_account)