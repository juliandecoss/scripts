# importing the module
import datetime
from json import dumps, loads


# declaringa a class
class obj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    return loads(dumps(dict1), object_hook=obj)


# initializing the dictionary
dictionary = {
    "user_id": 10004,
    "natural_person_id": 10005,
    "enterprise_id": 4,
    "source": "server",
    "email": "juliandecoss@gmail.com",
    "phone": str("9611230729"),
    "first_name": "Julian David",
    "last_name": "Julian David",
    "last_name1": "De Coss",
    "last_name2": "Espinosa",
    "enterprise_customer_type": "",
    "timestamp": datetime.datetime.now().isoformat(),
    "screen": "https://konfio.mx/mi/login",
    "utm_source": "",
    "utm_medium": "",
    "utm_campaign": "",
    "utm_term": "",
    "utm_content": "",
    "domain": "",
    "stage": "",
    "action": "",
}

obj1 = dict2obj(dictionary)
print(obj1.user_id)
obj1.__dict__
