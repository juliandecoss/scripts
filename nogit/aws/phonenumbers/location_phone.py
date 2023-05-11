import requests
from pprint import pprint
def get_location(phone_number):
    url = f'https://phonetracker-geek.com/{phone_number}'
    response = requests.get(url)
    location = response.json()
    return location

lo = get_location("9611230729")
pprint(lo)
breakpoint()