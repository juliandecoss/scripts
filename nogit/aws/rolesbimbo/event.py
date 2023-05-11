import datetime

event = {'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-length': '493',
                                      'content-type': 'application/x-amz-json-1.1',
                                      'date': 'Fri, 25 Mar 2022 14:45:56 GMT',
                                      'x-amzn-requestid': '3f8764eb-5ea6-4cb4-8e5d-3691bc7e4026'},
                      'HTTPStatusCode': 200,
                      'RequestId': '3f8764eb-5ea6-4cb4-8e5d-3691bc7e4026',
                      'RetryAttempts': 0},
 'User': {'Attributes': [{'Name': 'sub',
                          'Value': 'def5b692-5ed3-48c1-b365-c770bb48b54b'},
                         {'Name': 'email_verified', 'Value': 'true'},
                         {'Name': 'name', 'Value': 'SEGUNDO'},
                         {'Name': 'phone_number', 'Value': '+5255555555'},
                         {'Name': 'custom:paternal_last_name',
                          'Value': 'User by Admin'},
                         {'Name': 'email', 'Value': 'decossjulian@gmail.com'}],
          'Enabled': True,
          'UserCreateDate': datetime.datetime(2022, 3, 25, 8, 45, 55, 560000),
          'UserLastModifiedDate': datetime.datetime(2022, 3, 25, 8, 45, 55, 560000),
          'UserStatus': 'FORCE_CHANGE_PASSWORD',
          'Username': 'def5b692-5ed3-48c1-b365-c770bb48b54b'}}
for attr in event["User"]["Attributes"]:
  if attr["Name"] == "sub":
      sso_id = attr["Value"]
      break
breakpoint()