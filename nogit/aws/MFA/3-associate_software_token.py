import boto3
import json
import qrcode
from MFA_CONSTANTS import ACCESS_TOKEN
client = boto3.client('cognito-idp', region_name = 'us-west-2')
access_token = ACCESS_TOKEN
email = "konfioauth@gmail.com"

#ASOCIAR EL TOKEN
response =  client.associate_software_token(
    AccessToken = access_token
    )

print(json.dumps(response, sort_keys=True, indent=4))
secret_code = response["SecretCode"]
#CREAR QR
string_to_qr= f"otpauth://totp/Konfio ({email})?secret={secret_code}"
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)
qr.add_data(string_to_qr)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
print("QR CREADO")
img.save("qrTECHLAND.png")