from requests import Response, get
from urllib.parse import urlencode
"https://sso-admin-konfio-dev.auth.us-west-2.amazoncognito.com/login?client_id=137ff7lhsd5dvs7odetc1jdq6k&response_type=code&scope=email+openid+profile&redirect_uri=https://devbo.konfio.mx"
def cognito_oauth_authorize(payload: dict) -> Response:
    base_url = "https://sso-admin-konfio-dev.auth.us-west-2.amazoncognito.com"
    print(f"Julian:{payload}")
    response = get(f"{base_url}/oauth2/authorize", params=payload)
    breakpoint()
    status_code = response.status_code
    url_error = "error" in response.url
    if status_code != 200 or url_error:
        status_code = 400 if url_error else status_code
        raise Exception
    return response

#cognito_oauth_authorize({"client_id":"137ff7lhsd5dvs7odetc1jdq6k","response_type":"code","scope":"email openid profile","redirect_uri":"https://devbo.konfio.mx"})
"{'client_id': '137ff7lhsd5dvs7odetc1jdq6k', 'redirect_uri': 'https://devbo.konfio.mx', 'response_type': 'code', 'scope': 'openid profile email', 'user_type': 'user_admin'}"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#user_agent= "Sso-Konfio/1.0.0"
# header variable
headers = { 'user-agent' : user_agent }
url_web = "https://sso-admin-konfio-dev.auth.us-west-2.amazoncognito.com/oauth2/authorize?client_id=137ff7lhsd5dvs7odetc1jdq6k&redirect_uri=https://devbo.konfio.mx&response_type=code&scope=openid%20profile%20email&user_type=user_admin"
response = get("https://sso-admin-konfio-dev.auth.us-west-2.amazoncognito.com/oauth2/authorize",params={'client_id': '137ff7lhsd5dvs7odetc1jdq6k', 'redirect_uri': 'https://devbo.konfio.mx', 'response_type': 'code', 'scope': 'openid profile email'},headers=headers)# 'user_type': 'user_admin'
print(response.url)
breakpoint()
