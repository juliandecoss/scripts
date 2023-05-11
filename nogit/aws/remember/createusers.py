import boto3
from time import time_ns
from faker import Faker
faker = Faker()
Faker.seed(15)
client = boto3.client('cognito-idp', region_name = 'us-west-2')
#client_id = '2jmdtgc74olv85tr1agm3btoi8'
#user_pool = 'us-west-2_VODHRFn7A'
client_id = '2v3tko99u3eiid4hie80udvclk'
user_pool = 'us-west-2_PqrIVeNNd'

user='juligan_2911@hotmail.com'
pas='Tests@123'
emails =[]
start_time= time_ns()

create_account= client.sign_up(
    ClientId=client_id,
    Username=user,
    Password=pas,
    UserAttributes=[
        {
            "Name":"phone_number",
            "Value": "+529611230729",
        },
        {
            "Name":"name",
            "Value": faker.first_name(),
        },
        {
            "Name":"email",
            "Value":user,
        },
        {
            "Name":"custom:paternal_last_name",
            "Value": faker.last_name_male(),
        },
    ]
)
""" {
    "Name":"custom:paternal_last_name",
    "Value": faker.last_name_male(),
},
{
    "Name":"custom:maternal_last_name",
    "Value": faker.last_name_female(),
}, """