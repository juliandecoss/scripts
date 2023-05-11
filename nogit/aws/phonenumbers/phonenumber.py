from phonenumbers import NumberParseException, parse,format_number, PhoneNumberFormat,geocoder
from phonenumbers.timezone import time_zones_for_number
from phonenumbers.geocoder import description_for_number
from faker import Faker
from random import randint
faker = Faker()

CONTINENTS_BLOCKED_TO_SEND_SMS = ["Africa","Asia"]
COUNTRIES_BLOCKED_TO_SEND_SMS = []
  
def verify_sms_destination(phone_number:str)->None:
    try:
        phone = parse(phone_number)
        continent, capital_city = time_zones_for_number(phone)[0].split("/")
        print(continent)
        print(capital_city)
    except NumberParseException as e:
        print(f"otp:phone:invalid:{phone_number}:{e}")
        continent = ""
        country = ""
    if continent in CONTINENTS_BLOCKED_TO_SEND_SMS:
        print(f"otp:{phone_number}:invalid:continent:{continent}:country:{capital_city}:to:send:sms")
        raise Exception
    if country in COUNTRIES_BLOCKED_TO_SEND_SMS:
        print(f"otp:{phone_number}:invalid:country:{capital_city}:continent:{continent}:to:send:sms")
        raise Exception
    return
phones = ["+5112412341","+420731961110","+529611230729","+525510819482","+2917652499","+6289522260000",]
try:
    verify_sms_destination("+5491122744559")
except:
    ""
# for phone in phones:
#     phone = parse(phone)
#     print(f"+{phone.country_code}")
#     print(phone.national_number)
# AFGHANISTAN_AREA_CODES = ["070","071","072","073","074","075","076","077","078","079"] # seven digits for mexico area_code+faker.msisdn()[:7] AF
# INDONESIA_AREA_CODES = ["895", "896", "897", "898", "899"] # seven digits for mexico area_code+faker.msisdn()[:7] ID
# ERITREA_AREA_CODES = ["8"] # ER 6 digits ER
# COUNTRIES = {"Afghanistan":{"code":"AF","digits":7,"area":AFGHANISTAN_AREA_CODES},"Indonesia":{"code":"ID","digits":7,"area":INDONESIA_AREA_CODES},"Eritrea":{"code":"ER","digits":6,"area":ERITREA_AREA_CODES}}
# for country in COUNTRIES.keys():
#     country_info = COUNTRIES[country]
#     area_codes = country_info["area"]
#     area_code = area_codes[randint(0,len(area_codes)-1)]
#     my_number = parse(area_code+faker.msisdn()[:country_info['digits']], country_info['code'])
#     real_number=format_number(my_number, PhoneNumberFormat.E164)
#     print(real_number)
#     try:
#         ""
#         verify_sms_destination(real_number)
#     except:
#         ""

# for area_code in ERITREA_AREA_CODES:
#     my_number = parse(area_code+faker.msisdn()[:6], "ER")
#     real_number=format_number(my_number, PhoneNumberFormat.E164)
#     try:
#         ""
#         verify_sms_destination(real_number)
#     except:
#         ""
#     #print("ALL COOL")
