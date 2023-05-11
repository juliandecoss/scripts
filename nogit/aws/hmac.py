from math import floor
from pprint import pprint
""" challenge_name = "SMS_MFA"
data = {
    "ChallengeName": "challenge_name",
    "ChallengeParameters": {"USER_ID_FOR_SRP": "faker.uuid4()"},
    "Session": "aker.sha256()",
    "ResponseMetadata": "mock_response_metadata(**kwargs),"
}
if challenge_name == "SMS_MFA":
    data["ChallengeParameters"].update({"CODE_DELIVERY_DESTINATION":f"********999"})
pprint(data) """
email = "juliandecoss@gmail.com"
masked_start = floor(len(email)/4)
masked_end = masked_start*2
email_masked = email[:masked_start] + masked_start*"*" + email[masked_end:]
print(email_masked)
print(email)
print(len(email))
