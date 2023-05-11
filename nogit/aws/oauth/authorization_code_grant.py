from requests import get, post
from json import dumps
from urllib.parse import urlencode
from requests.structures import CaseInsensitiveDict
CLIENT_ID="us-west-2_PqrIVeNNd"
RESPONSE_TYPE="code"
#RESPONSE_TYPE="token"
REDIRECT_URI="https://dev.konfio.mx/mi/dashboard/negocio/staff/agregar"
SCOPE="openid"
CLIENT_ID = "2col44s778aeog1a4obbij66co"
SECRET = "1qrorupfvpq0igrfiiq0tg5b5obp0bn6s76607rqt717ote9515k"
DOMAIN_NAME = "sso-konfio-dev.auth.us-west-2.amazoncognito.com"
USERNAME="jugui@gmail.com"
PASSWORD="test123"

url = f"https://{DOMAIN_NAME}/oauth2/authorize?response_type={RESPONSE_TYPE}&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
url = "https://sso-konfio-dev.auth.us-west-2.amazoncognito.com/oauth2/authorize?response_type=code&client_id=2col44s778aeog1a4obbij66co&redirect_uri=https%3A%2F%2Fdev.konfio.mx%2Fmi%2Fdashboard%2Fnegocio%2Fstaff%2Fagregar&scope=https%3A%2F%2Fplatform.konfio.mx%2Fcore%2Fprofile.admin+openid+profile&state=2d00c06a-6741-4852-84cf-c58121a31746"
response = get(url,allow_redirects=False)
url_redirect = response.headers["Location"]
response_cookie = "c539fcae-b614-4fa0-b991-9606cdf68e05"
cookie = 'XSRF-TOKEN='+ response_cookie
headers = {}
headers["Cookie"] = cookie+"; csrf-state=""; csrf-state-legacy="""
headers["origin"]= "https://sso-konfio-dev.auth.us-west-2.amazoncognito.com"
headers["referer"] = "https://sso-konfio-dev.auth.us-west-2.amazoncognito.com/login?response_type=code&client_id=2col44s778aeog1a4obbij66co&redirect_uri=https://dev.konfio.mx/mi/dashboard/negocio/staff/agregar&scope=openid"
headers["content-type"]= "application/x-www-form-urlencoded"

data = {"_csrf":response_cookie,"username":USERNAME,"password":PASSWORD,"signInSubmitButton":"Sign in","cognitoAsfData":"eyJwYXlsb2FkIjoie1wiY29udGV4dERhdGFcIjp7XCJVc2VyQWdlbnRcIjpcIk1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85NS4wLjQ2MzguNjkgU2FmYXJpLzUzNy4zNlwiLFwiRGV2aWNlSWRcIjpcInJoMmV3c2E3OTJpdm8zdDZjODFvOjE2MzY1NzkzMTc1NTlcIixcIkRldmljZUxhbmd1YWdlXCI6XCJlbi1VU1wiLFwiRGV2aWNlRmluZ2VycHJpbnRcIjpcIk1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85NS4wLjQ2MzguNjkgU2FmYXJpLzUzNy4zNlBERiBWaWV3ZXI6Q2hyb21lIFBERiBWaWV3ZXI6Q2hyb21pdW0gUERGIFZpZXdlcjpNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyOldlYktpdCBidWlsdC1pbiBQREY6ZW4tVVNcIixcIkRldmljZVBsYXRmb3JtXCI6XCJNYWNJbnRlbFwiLFwiQ2xpZW50VGltZXpvbmVcIjpcIi0wNjowMFwifSxcInVzZXJuYW1lXCI6XCJqdWd1aUBnbWFpbC5jb21cIixcInVzZXJQb29sSWRcIjpcIlwiLFwidGltZXN0YW1wXCI6XCIxNjM2NTc5MzE3NTU5XCJ9Iiwic2lnbmF0dXJlIjoicm5pSmNoQ2hNSGkvUkx1QXByNVhCWmMrdldpY2ExRFhPNmhiMk5EUUJCaz0iLCJ2ZXJzaW9uIjoiSlMyMDE3MTExNSJ9"}
data = dumps(data)
response2 = post(url_redirect,allow_redirects=False,headers=headers, data=data)
code = response2.headers["Location"]
breakpoint()