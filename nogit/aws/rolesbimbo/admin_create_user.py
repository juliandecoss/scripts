import boto3
import json
import pprint
# MessageAction='RESEND',
user_pool_id = 'us-west-2_PqrIVeNNd'
email = 'decossjulian@gmail.com'
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
                    "DesiredDeliveryMediums":['EMAIL'],
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
""" UserPoolId=user_pool_id,
Username=email,
UserAttributes=[
    {
    "Name":"phone_number",
    "Value": "+5255555555",
    },
    {
        "Name":"name",
        "Value": "SEGUNDO",
    },
    {
        "Name":"custom:paternal_last_name",
        "Value": "User by Admin",
    },
    {
        "Name":"email",
        "Value":email,
    },
],
ForceAliasCreation=False,
DesiredDeliveryMediums=['EMAIL'],
ClientMetadata={"origin": "konfio.mx"} """