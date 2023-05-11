from requests import get
from pprint import pprint

i= ""
while i == "":
    response = get("https://www.footballrocker.com")
    pprint(response.status_code)
    #pprint(response.text)