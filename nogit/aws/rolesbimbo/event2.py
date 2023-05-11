event={
  "version": 1,
  "triggerSource": "CustomMessage_AdminCreateUser",
  "region": "<region>",
  "userPoolId": "<userPoolId>",
  "userName": "<userName>",
  "callerContext": {
      "awsSdk": "<calling aws sdk with version>",
      "clientId": "<apps client id>",
      
  },
  "request": {
      "userAttributes": {
          "phone_number_verified": False,
          "email_verified": True,
          "custom_paternal_last_name":"Espinosa",
          "custom_maternal_last_name":"De Coss",
          "name":"Julian",
          "email":"juligan_2911@hotmail.com"
      },
      "codeParameter": "####",
      "usernameParameter": "juligan_2911@hotmail.com"
  },
  "response": {
      "smsMessage": "<custom message to be sent in the message with code parameter and username parameter>",
      "emailMessage": "<custom message to be sent in the message with code parameter and username parameter>",
      "emailSubject": "<custom email subject>",
  }
}