from ast import And
from atexit import register
from pickle import FALSE, TRUE
import boto3
import time
import dbm
import shelve

class SSO:
    clientType = "public"
    sso_url = ""
    sso_region = ""
    grant_type = "urn:ietf:params:oauth:grant-type:device_code"
    role_name = ""
    clientExpired = True
    tokenExpired = True
    refreshToken = False
    deviceExpired = True

    def __init__(self, clientName):
        print("SSO Init")
        self.clientName = clientName

        self.db=shelve.open("sso-konfio.db", "c")
        self.sso_url = "https://d-9067baa0dc.awsapps.com/start"
        self.sso_region = "us-east-1"
        self.role_name = "pf-read-only"

        self.sso_oidc = boto3.client('sso-oidc', region_name=self.sso_region)

    def login(self):
        print("Login")
        print(time.time())
        if ('expiresIn' in self.db) and (time.time() - 900) < int(self.db["expiresIn"]):
            print("expiresIn")
            self.tokenExpired = False

        if ('clientSecretExpiresAt' in self.db) and (time.time() - 900) < int(self.db["clientSecretExpiresAt"]):
            print("clientSecretExpiresAt")
            self.clientExpired = False

        if ('DeviceExpiresIn' in self.db) and (time.time() - 60) < int(self.db["DeviceExpiresIn"]):
            print("DeviceExpiresIn")
            self.deviceExpired = False

        print("refreshToken")
        print(self.refreshToken)

        if self.tokenExpired:
            if self.clientExpired:
                print("Client expired")
                self.registerClient()
                self.registerDevice()
                print("Authorize Device")
                print(self.db["verificationUriComplete"] + "\n")
                input("Press Enter to continue...")
                self.createToken()
            else:
                if self.deviceExpired:
                    self.registerDevice()
                    print("Authorize Device")
                    print(self.db["verificationUriComplete"] + "\n")
                    input("Press Enter to continue...")
                self.createToken()


    def registerClient(self):
        print("Register Client")
        print(self.clientName)
        print(self.clientType)
        sso_client = self.sso_oidc.register_client(
            clientName=self.clientName,
            clientType=self.clientType,
        )
        self.db["clientId"] = sso_client["clientId"]
        self.db["clientSecret"] = sso_client["clientSecret"]
        self.db["clientIdIssuedAt"] = str(sso_client["clientIdIssuedAt"])
        self.db["clientSecretExpiresAt"] = str(sso_client["clientSecretExpiresAt"])
        #self.db["authorizationEndpoint"] = sso_client["authorizationEndpoint"]
        #self.db["tokenEndpoint"] = sso_client["tokenEndpoint"]

    def registerDevice(self):
        print("Register Device")
        sso_device = self.sso_oidc.start_device_authorization(
            clientId=str(self.db["clientId"]),
            clientSecret=str(self.db["clientSecret"]),
            startUrl=self.sso_url
        )
        self.db["deviceCode"] = sso_device["deviceCode"]
        self.db["userCode"] = sso_device["userCode"]
        self.db["verificationUri"] = sso_device["verificationUri"]
        self.db["verificationUriComplete"] = sso_device["verificationUriComplete"]
        self.db["DeviceExpiresIn"] = int(time.time() + sso_device["expiresIn"])
        self.db["interval"] = sso_device["interval"]

    def createToken(self):
        
        sso_token = self.sso_oidc.create_token(
            clientId=self.db["clientId"],
            clientSecret=self.db["clientSecret"],
            grantType=self.grant_type,
            deviceCode=self.db["deviceCode"],
        )

        self.db["accessToken"] = sso_token["accessToken"]
        self.db["tokenType"] = sso_token["tokenType"]
        self.db["expiresIn"] = int(time.time() + sso_token["expiresIn"])

   
    def listAccounts(self):
        client = boto3.client(
            'sso', 
            region_name=self.sso_region
        )

        response = client.list_accounts(
            #nextToken = '',
            maxResults=100,
            accessToken=self.db["accessToken"]
        )

        return response["accountList"]

    def loginAccount(self,accountId):
        client = boto3.client(
            'sso',
            region_name=self.sso_region
        )
        try:
            response = client.get_role_credentials(
                roleName="escalation-admin",
                accountId=accountId,
                accessToken=self.db["accessToken"]
            )
        except:
            try:
                response = client.get_role_credentials(
                    roleName="admin",
                    accountId=accountId,
                    accessToken=self.db["accessToken"]
                )
            except:
                response = client.get_role_credentials(
                    roleName="read-only",
                    accountId=accountId,
                    accessToken=self.db["accessToken"]
                )
                print("Error Role")

        return response["roleCredentials"]

    def getRegions(self,credentials):
        client = boto3.client(
            'ec2',
            aws_access_key_id=credentials["accessKeyId"],
            aws_secret_access_key=credentials["secretAccessKey"],
            aws_session_token=credentials["sessionToken"],
            region_name=self.sso_region
        )
        response = client.describe_regions()
        #print(response)
        return response["Regions"]

    def validateAccount(self, credentials):
        client = boto3.client(
            'sts',
            aws_access_key_id=credentials["accessKeyId"],
            aws_secret_access_key=credentials["secretAccessKey"],
            aws_session_token=credentials["sessionToken"]
        )
        response = client.get_caller_identity()
        print (response)

        

        
