from csv import reader
from phonenumbers import parse
from requests import post, put
from json import dumps

ACCESS_TOKEN = "eyJraWQiOiJXZGMralRJa2lIemQxejI4NGt1MGxvREM2bk5GS1o4TGdKXC9ldG9pemlpRT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZmY0MDdmNi0zM2I0LTQyY2ItYTcwMy1jZDhmODNkYjk2OTciLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy13ZXN0LTJfU0dIWGZ6Y3lOX0dvb2dsZSIsInVzZXJfYWRtaW4iXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfU0dIWGZ6Y3lOIiwidmVyc2lvbiI6MiwiY2xpZW50X2lkIjoiMmNzODVkdHExbnRuam5yYnR0OGJhdTdtZTUiLCJvcmlnaW5fanRpIjoiMGEzZGRlNmItZTJhNy00NDVhLTkxY2MtMDk5MzYyMDE3MDIwIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImF1dGhfdGltZSI6MTY2OTkxMDkwNCwiZXhwIjoxNjY5OTMyNTA0LCJpYXQiOjE2Njk5MTA5MDQsImp0aSI6IjcyYjUwODNjLTc4ZDQtNGZmYS1iZmEyLWM2YTAzNWViYzQxMSIsInVzZXJuYW1lIjoiZ29vZ2xlXzEwNjY2MDQ3MzE5NDI5OTk2NjA0NSJ9.URNO2yNXNztVXPRC3y1ZRHe-C1ExNlmkMx6Yj2LyFLeBOa8hnGf0DuW96jHCLIGt8oNYeI6SUvToLYJi5l9RNZpriNQ7QMXLyCw0jHcNu64D5pf1EFzIq5RaZiJ4HYyyO-LVyqfmKflgAgZEkwlgk8bAfDjbNQUeGgsOvxRTdLme9wisS7ie5NBsOdkdf0ad4IzJJ0PdB_yGzEgwhEsw8ibFSUFye67ZhBRJ51eMk4ubCSw6A9n7ENuwCLifAsPnGiPmy6imoddvfCclltvqo2CzVq97z8lZUxSkxPzI9QolMvrMp9PkpIxOdIZHtcHBTEZjRKtbAp0CABxHF-esBg"
with open("phonenumbers/numeros-ataque.csv", newline="") as file_with_emails:
    csv_reader = reader(file_with_emails, delimiter=",")
    for pos,row in enumerate(csv_reader):
        if pos != 0:
            phone_number = "+" + row[0]
            phone = parse(phone_number)
            url = "https://dev-platform.konfio.mx/core/entities/person/1441716/phone"
            payload = dumps({
                "number": str(phone.national_number),
                "comments": "Updated to PP",
                "typeId": 6,
                "statusId": 22,
                "countryCode": f"+{phone.country_code}",
                "createdByEmail": "system_process@konfio.mx"
            })
            headers = {
                'Origin': 'sso.konfio.mx',
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {ACCESS_TOKEN}"
            }
            response = put(url,headers=headers,data=payload)
            if response.status_code == 200:
                print(f"Mobile: {pos} successful updated")
            else:
                print(f"Mobile: {pos} unsuccessful")

            url = "https://dev-platform.konfio.mx/core/verification/person/1441716/verification-code"
            payload={}
            headers = {
                'Origin': 'dev-sso.konfio.mx',
                'Authorization': f"Bearer {ACCESS_TOKEN}"
            }
            response = post(url,headers=headers,data=payload)
            if response.status_code == 200:
                print(f"Mobile: {pos} SOMETHING WENT WRONG THE SMS WAS SENT")
            else:
                re = response.json()
                print(f"Mobile: {pos} the sms was blocked:{re['error']['message']} : requestId: {re['requestId']}")
            print("##########################")