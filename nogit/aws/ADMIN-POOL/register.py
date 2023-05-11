import boto3
import json
import pprint
# MessageAction='RESEND',
user_pool_id = 'us-west-2_SGHXfzcyN'
client_id = '137ff7lhsd5dvs7odetc1jdq6k'
client_secret = '114gkjkp3ooug5hdl198havs95l1d7quafultapcba3g61t4v3rq'

password='Tests@123'
phone='+529611230729'
email = 'juliandecoss@gmail.com'
user_a = [
        {"Name":"phone_number","Value": "+5255555555"},
        { "Name":"name","Value": "SEGUNDO"},
        {"Name":"custom:paternal_last_name","Value": "User by Admin"},
        {"Name":"email","Value":email,},
        {"Name":"email_verified","Value": "true"}
        ]

client = boto3.client('cognito-idp', region_name = 'us-west-2')
admin_create_attr = {"UserPoolId":user_pool_id,
                     "Username":email,
                     "UserAttributes":user_a+[{"Name":"email_verified","Value": "true"}],
                    #"DesiredDeliveryMediums":['EMAIL'],
                    #"TemporaryPassword":'Nonecesitashacerlo!2',
                   #"MessageAction" : "RESEND",
                    "ClientMetadata":{"origin": "legalrep_cards"},
    }
def create_user():
    respuesta = client.admin_create_user(**admin_create_attr)
    return respuesta
try:
    respuesta = create_user()
    pprint.pprint(respuesta)
except Exception as e:
    pprint.pprint(e)
    if e.__dict__.get("response",{}).get("Error",{}).get("Code",{}) == 'UsernameExistsException':
        print("THIS DUDE ALREADY EXISTS")
breakpoint()
