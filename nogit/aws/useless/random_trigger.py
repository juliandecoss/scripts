from random import randint

SMS_TRIGGER_SOURCE = {
    "registration": "CustomSMSSender_SignUp",
    "resend_code": "CustomSMSSender_ResendCode",
    "forgot_passwrod": "CustomSMSSender_ForgotPassword",
    "update_user": "CustomSMSSender_UpdateUserAttribute",
    "verify_user": "CustomSMSSender_VerifyUserAttribute",
    "registration_as_admin": "CustomSMSSender_AdminCreateUser",
    "account_notification": "CustomSMSSender_AccountTakeOverNotification",
    "sms_mfa": "CustomSMSSender_Authentication",
}
trigger_list = list(SMS_TRIGGER_SOURCE.keys())
trigger_list.remove("sms_mfa")
trigger_source = trigger_list[randint(0, len(trigger_list) - 1)]
print(trigger_list)
print(trigger_source)