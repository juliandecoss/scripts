import json
import sys
import boto3
import datetime
import csv


sys.path.append("../libs")

from sso import SSO

clientName = "jose.urias.konfio.mx"
sso_region = "us-east-1"

csv_rows = []

sso = SSO(clientName)

sso.login()

list_accounts = sso.listAccounts()

restrict = False

restrict_accounts = [
    "639547259187", #legacy-konfio-api
    "051790733337", #legacy-konfio-astro
    "437993981736", #legacy-konfio-data-governance
    "399968441508", #legacy-konfio-data-science
    "074242131296", #legacy-konfio-data-science-test
    "787241336849", #legacy-konfio-infosec
    "354773346676", #legacy-konfio-kss
    "925644926633", #legacy-konfio-kts
    "726101965919", #legacy-konfio-test
    "563241948955", #legacy-konfio-whatsapp
    "465640780896", #legacy-payments-core-prd
    "063975098981", #legacy-payments-sandbox
    "483705751555", #legacy-payments-sdlc
    "195917654559", #legacy-payments-switch-prd
    "180477243137", #180477243137
]

""" restrict_accounts = [
"483705751555", #legacy-payments-sandbox
] """

for account in list_accounts:

    if account["accountId"] not in restrict_accounts:
        continue

    print(account)

    print("Account Name: " + account["accountName"])
    print("Account ID: " + account["accountId"])
    credentials = sso.loginAccount(account['accountId'])
    
    print("GetRegions")
    regions = sso.getRegions(credentials)
    #print(regions)
    
    print("LoopRegions")
    for region in regions:
        if region["RegionName"] != "us-east-1" :
            continue
        print("\t Region: " + region["RegionName"])
        
       
        ##Start working

        iam = boto3.client(
            'iam',
            aws_access_key_id=credentials["accessKeyId"],
            aws_secret_access_key=credentials["secretAccessKey"],
            aws_session_token=credentials["sessionToken"],
            region_name=region["RegionName"]
        )
        iam_user = boto3.resource(
            'iam',
            aws_access_key_id=credentials["accessKeyId"],
            aws_secret_access_key=credentials["secretAccessKey"],
            aws_session_token=credentials["sessionToken"],
            region_name=region["RegionName"]
        )

        paginator = iam.get_paginator('list_users')

    marker = None

    response_iterator = paginator.paginate(
        PaginationConfig={
            'PageSize': 100,
            'StartingToken': marker
        }
    )

    for page in response_iterator:
        users = page['Users']
        for user in users:

            #print(json.dumps(user, indent=4, sort_keys=True, default=str))
            print(user["UserName"])
            
            user_resource = iam_user.User(user["UserName"])
            login_profile = iam_user.LoginProfile(user["UserName"])

            try:
                login_profile_create_date_temp = login_profile.create_date
                login_profile_create_date = "Active"
            except:
                login_profile_create_date = "None"

            print(login_profile_create_date)

            i = 0 
            access_key_0 = ""
            access_key_1 = ""

            user_access_keys = iam.list_access_keys(
                UserName=user["UserName"]
            )

            for key in user_access_keys["AccessKeyMetadata"]:

                user_access_key_details = iam.get_access_key_last_used(
                    AccessKeyId=key["AccessKeyId"]
                )

                user_access_key_id =key["AccessKeyId"] 
                user_access_key_status=key["Status"]
                try:
                    user_access_key_last_used_date = user_access_key_details["AccessKeyLastUsed"]["LastUsedDate"]
                    user_access_key_last_used_service = user_access_key_details["AccessKeyLastUsed"]["ServiceName"]
                    user_access_key_last_used_region = user_access_key_details["AccessKeyLastUsed"]["Region"]
                except:
                    user_access_key_last_used_date = "None"
                    user_access_key_last_used_service = "None"
                    user_access_key_last_used_region = "None"
                
                
                csv_rows.append(
                    [  
                        account["accountId"],
                        account["accountName"],
                        user["UserName"],
                        login_profile_create_date,
                        user_access_key_id,
                        user_access_key_status,
                        user_access_key_last_used_date,
                        user_access_key_last_used_service,
                        user_access_key_last_used_region,
                    ]
            )

fields = [
    'AccountId',
    'AccountName',
    'UserName',
    "Console",
    "AK_0_id",
    "AK_0_status",
    "AK_0_last_used",
    "AK_0_service",
    "AK_0_region",
    "AK_1_id",
    "AK_1_status",
    "AK_1_last_used",
    "AK_1_service",
    "AK_1_region",
]

with open('iam-list-'+datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.csv', 'w') as f:

    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(csv_rows)


