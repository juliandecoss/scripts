from boto3 import client
from pprint import pprint


sso_client = client('sso')
response = sso_client.list_account_roles(
    nextToken='string',
    maxResults=123,
    accessToken='string',
    accountId='string'
)
breakpoint()