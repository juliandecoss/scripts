from requests import post
from urllib.parse import urlencode
from time import sleep
set_usuarios = [{"identity":"juligan_2911@hotmail.com","credential":"Tests@123"},{"identity":"jorgect99@gmail.com","credential":"Tests123!"},{"identity":"jorgekonfi@gmail.com","credential":"Tests123!"}]
identity = ""
url = "https://dev-sso.konfio.mx/login"
payload = {
    "clientId":"2v3tko99u3eiid4hie80udvclk"
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
for i in range(1,20):
    for i in set_usuarios:
        payload["identity"] = i["identity"]
        payload["credential"] = i["credential"]
        payload=urlencode(payload)
        response = post(url, headers=headers, data=payload)
        print(response.json()["message"])
        sleep(3)
