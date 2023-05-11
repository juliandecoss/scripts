from csv import reader
from time import time
import json
from boto3 import client
from botocore.config import Config

cognito = client("cognito-idp", config=Config(region_name="us-west-2"))
#DESVERIFICAR LOS USUARIOS

user_pool_id = "us-west-2_PqrIVeNNd" #DEV
#user_pool_id = "us-west-2_VODHRFn7A" #PROD
start_time = time()
line_count = 0
with open("/Users/intern/Desktop/cognito/reset_users/usuarios.csv", newline="") as file_with_emails:
    csv_reader = reader(file_with_emails, delimiter=",")
    for row in csv_reader:
        line_count +=1
        user_name = row[0] #AQUI SE AGREGA EL ROW EN EL QUE ESTÁ EL EMAIL
        print(f"EMAIL A RESETEAR:{user_name}")
        if line_count !=0:
            #SIGN-OUT USER
            try:
                response = cognito.admin_user_global_sign_out(
                    UserPoolId=user_pool_id,
                    Username= user_name
                )
                print(f"THIS EMAIL HAS BEEN SIGNED OUT {user_name}")
                print(json.dumps(response, sort_keys=True, indent=4))
            except Exception as e:
                print(f"THIS USER CANT BE SIGNED OUT {user_name}")
                print(e)
            #RESET THE PASSWORD
            try:
                response = cognito.admin_reset_user_password(
                    UserPoolId=user_pool_id, Username=user_name
                )
                print(json.dumps(response, sort_keys=True, indent=4))
            except Exception as e:
                print(f"{user_name}CANT RESET THIS PASSWORD")
                print(e)