from email import header
from requests import post
from base64 import b64encode
from urllib.parse import urlencode

url = "https://dev-sso.konfio.mx/token"
CLIENT_ID = "mh7m45lopkh30ipqbtfmvg0rd"
CLIENT_SECRET = "1erub5hop4bcfnrjjbvb042j8n0doiek9156tl9sf24obraujmff"
basic_header = b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
payload = urlencode({
    "grant_type":"client_credentials",
    "client_id": CLIENT_ID,
})
headers = {
  'Authorization': 'Basic {token}'.format(token=basic_header),
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = post(url, headers=headers, data=payload)
breakpoint()
response.json()["accessToken"]
#print(response.text)