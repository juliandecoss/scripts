import boto3
import json
import pprint
# MessageAction='RESEND',
user_pool_id = 'us-west-2_PqrIVeNNd'
email = 'juligan_2911@hotmail.com'

client = boto3.client('cognito-idp', region_name = 'us-west-2')
#"UserAttributes":[{"Name":"email","Value":email}],
admin_create_attr = {"UserPoolId":user_pool_id,
                     "Username":email,
                     "UserAttributes":[{"Name":"email","Value":email}],
                     "DesiredDeliveryMediums":['EMAIL'],
                     "MessageAction":'RESEND',
                     "ClientMetadata":{"origin": "legalrep_cards"},
    }
def create_user():
    respuesta = client.admin_create_user(**admin_create_attr)
    return respuesta
try:
    respuesta = create_user()
    pprint.pprint(respuesta)
    print(respuesta["User"]["UserStatus"])
    print(respuesta["User"]["Username"])
except Exception as e:
    pprint.pprint(e)
    breakpoint()
    if e.__dict__.get("response",{}).get("Error",{}).get("Code",{}) == 'UsernameExistsException':
        print("THIS DUDE ALREADY EXISTS")