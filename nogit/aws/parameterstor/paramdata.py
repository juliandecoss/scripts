from urllib.parse import urlencode
data={"identity": "jugui@konfio.mx",
    "clientId": "2a1uak2rhj1kuilvnpg0kdqjn1",
    "name": "Beethoven",
    "paternalLastName": "Tchaikovsky",
    "maternalLastName": "K-paz de la sierra"}
print(urlencode(data))