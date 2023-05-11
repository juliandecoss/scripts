import os 
from twilio import Client,TwilioException
jjj="+529611230729"
kkk = '+420731961110'

phone_to_send=os.environ.get('TWILIO_MYNUMBER')
account_sid=os.environ.get('TWILIO_SID')
account_token=os.environ.get('TWILIO_TOKEN')
twilio_number=os.environ.get('TWILIO_NUMBER')

twclient=Client(account_sid,account_token)
try:
    message = twclient.messages.create(   
                                to=kkk,
                                body="Baubi i love you",  
                                from_="+12318215440"
        )
except Exception as e:
    if e.__dict__["code"]==21408:
        print("We dont support this country")
    breakpoint()
    print(e.args)