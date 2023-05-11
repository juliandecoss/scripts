import requests

url = "https://dev-sso.konfio.mx/authorize?response_type=code&client_id=2col44s778aeog1a4obbij66co&redirect_uri=https%3A%2F%2Fkonfio.mx%2Fme%2Fempresa%2F&scope=https%3A%2F%2Fplatform.konfio.mx%2Fcore%2Fprofile.admin"
headers = {}
payload={}

response = requests.request("GET", url, headers=headers, data=payload, allow_redirects=False)

print(response.text)
print(response.headers)
print(response.status_code)