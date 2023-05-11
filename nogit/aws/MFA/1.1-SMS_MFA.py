import boto3
import json

username='23daf9dd-117d-48f0-9a41-3ed5fd6a74b0'
client = boto3.client('cognito-idp', region_name = 'us-west-2')
#client_id = '2v3tko99u3eiid4hie80udvclk'
client_id = '7jgtj79dk97givsn4or6o20d1f'
response_mfa_challenge =  client.respond_to_auth_challenge(
        ClientId=client_id,
        ChallengeName='SMS_MFA',
        Session="AYABeNY3b2AB43LjsmPe7qM7T10AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjowMTU3MzY3MjcxOTg6a2V5LzI5OTFhNGE5LTM5YTAtNDQ0Mi04MWU4LWRkYjY4NTllMTg2MQC4AQIBAHiLcRcG62Mb19KUM6qQUoajwNOF_-4FakXKLIP1RcBYjQFZT366ahthcwx_RUUPdOgKAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMd-a08qgB6CcQsNhfAgEQgDuzovrJK-49D5FDszlUmMYMtDguRLuAui9y6nHMdXzgOiElrStELJre4VN4XkfsPt6LsbifKKrgvvNSZwIAAAAADAAAEAAAAAAAAAAAAAAAAABCp250A3uwnMhov9SR5dbN_____wAAAAEAAAAAAAAAAAAAAAEAAAIAC6HkfXQoRBc27MuZ-5LwBve9KjjaoVytJIF62qAFpDLm4TKvr0NYDdT18H7YWwYBdZs0BmsvHqHL2Sn6m16Yzf5eXW7AxzOt4d8rLLM1fpnidMaNuZXuJ_edT1L2J_XexFcLEvSAMN0wnEP_z0RcuQJ3oVfhjhBdaq9Xw-x7C6ecexrIAk-JcwKT4mDx9F31EqR4QgsuhtWZy640ut6fI7UgQvB78bn3c3G7QoZrjc-yHXSKKGTU6xT1qCqkNUe-PZyewdXxa7pCXz4gj0o6HBZWUCTPEZFblCqTMlUD0nqZdimRiEPhUA1X5WIrTp8t2FMgVyG3d2wU8Hhyzl_Xn4Z0BzAH6YkdHJgTcAKJt58JDqVUtNVJhNZFcbniwCVZDOzs1aR8gx9W68rr42owqHH3J8Aamo_GtduagnlRmqtvnhEE4rN0LB6CZEW7-DXiohZp0i0z6Q6UUE4AE6AJ7i2LQFo-gwJLj2yNTwmcggEvOtQzT2HCnd9S5LyhQtCgCJ2d4DaX3v1IimsYThfUZAGI2ZpY6fY10nr58Srasm_VDrtzxgzEpzjG1hnmwx9H3Swjd2tAU4x-5rXzSOLRX5nwzwGh8S8syCD3dVuWDuGfuGbgEl1yGS6h1CoGcJtGWJylK9OYFMmKfyKGOkZEETKEulWHBLGwqDZ1rIMag9iZa6eUFeugejDYCTPBytba",
        ChallengeResponses={
            'USERNAME': username,
            'SMS_MFA_CODE':"758630"
            }
        )

print(json.dumps(response_mfa_challenge, sort_keys=True, indent=4))