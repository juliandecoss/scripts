from csv import writer
from datetime import datetime
from http import client
from os import environ
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cw_insights import cw_run_query,parse_cw_results
from send_hook import send_hook_to_prueba, send_hook_to_act_mgmmt
import smtplib
from pprint import pprint
from global_constants import DEPRECATED_APP_CLIENTS,APP_CLIENTS


EMAIL_ADDRESS='decossjulian@gmail.com'
EMAIL_PASSWORD='Netoesguey2!'
environ["STAGE"] = "prod"
environ["AWS_REGION"] = "us-west-2"
FILE_PATH = f'{environ.get("HOME")}/desktop/cognito/cloudwatch/reporte.csv'
START_DATE = datetime.strptime("2022-05-16 00:00 -0600", "%Y-%m-%d %H:%M %z")
END_DATE = datetime.strptime("2022-05-23 23:59 -0600", "%Y-%m-%d %H:%M %z")
LOG_GROUPS = ["custom-sender-trigger"]
ALL_USERS = f"""
filter stage = "{environ.get("STAGE")}"
| stats count_distinct(email)
"""
USERS_AUTHENTICATED_BY_LOGIN = """
filter stage = "prod" and statusCode = 200
| stats count_distinct(username) as usuarios by loginType
| sort loginType asc
"""
USER_WITH_CHALLENGE = """
filter stage = "prod" and statusCode = 200
| stats count_distinct(username) as usuarios
"""
USERS_USING_EMAIL = """
filter stage = "prod" and statusCode = 200 and deliveryMedium = 'email'
| stats count_distinct(username) as usuarios
"""
ALL_USERS_SUCCESS = f"""
filter stage = "{environ.get("STAGE")}" and statusCode = 200
| stats count_distinct(email)
"""
REFRESH_BY_APP = """
filter stage = "prod" and statusCode = 200 
| stats count_distinct(email) as usuarios by clientId
| sort clientId asc
"""
SNS_SPEND = """
filter deliveryMedium = "sms" and statusCode = 200
| stats count(*) as smsEnviados
| display smsEnviados * 0.0126 as precio
"""
LOGIN_PERFORMANCE = """
filter stage = "prod" and statusCode = 200
| stats avg(duration) as performance by loginType
| sort loginType asc
"""
LOGIN_ERRORS = """
filter stage = "prod" and statusCode != 200
| stats count(*) as quantity by reason
| sort quantity desc
| limit 6
"""
APP_TRAFFIC = """
filter stage = "prod" and statusCode = 200
| stats count_distinct(email) as traffic by clientId
| sort traffic desc
| limit 5
"""
NEW_MFA_USERS ="""
filter stage = "prod" and statusCode = 200
| stats count_distinct(email) as users
"""
def parse_login_errors(error:dict)->dict:
    reason = error.get("reason","")
    if reason.startswith("InitiateAuthException"):
        real_reason = reason.split(":")[-1:][0]
        error["reason"] = real_reason
    return error

def get_app_client_name(app_data:dict)->dict:
    client_id = app_data["clientId"]
    if DEPRECATED_APP_CLIENTS.get(client_id,""):
        client_id = DEPRECATED_APP_CLIENTS[client_id]
    app_data["app_name"] = APP_CLIENTS[client_id]
    return app_data
def get_login_data():
    print("searching...\n")
    
    new_mfa_users = cw_run_query(
        lambda_groups=["mfa"], query=NEW_MFA_USERS, start_date=START_DATE, end_date=END_DATE
    )
    new_mfa_parsed = parse_cw_results(new_mfa_users)
    new_users = new_mfa_parsed[0]["users"]

    pprint(new_mfa_parsed)
    breakpoint()
    
    return


if __name__ == "__main__":
    get_login_data()