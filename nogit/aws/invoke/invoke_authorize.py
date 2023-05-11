
import boto3
import json
from urllib.parse import urlencode
from pprint import pprint
client = boto3.client('lambda')
scopes_completos = "openid profile https://platform.konfio.mx/core/profile.admin https://platform.konfio.mx/core/enterprise.admin https://platform.konfio.mx/core/loan.admin https://platform.konfio.mx/core/cards.admin https://platform.konfio.mx/core/kopay.admin https://platform.konfio.mx/core/payments.admin https://platform.konfio.mx/core/inventory.admin https://platform.konfio.mx/core/reporting.admin"
event = {
    "path": "/authorize",
    "headers": {"PLATFORM-ORIGIN": "PLATFORM-CORE"},
    "queryStringParameters": {"response_type":"code",
                             "client_id":"2col44s778aeog1a4obbij66co",
                             "redirect_uri":"https://dev.konfio.mx/mi/dashboard/negocio/staff/agregar",
                             "scope":scopes_completos},
    "requestContext": {"httpMethod": "GET", "stage": "dev","path":"/authorize"},
    "body":'',
}

response = client.invoke(
    FunctionName='sso-oauth-token',
    Payload=json.dumps(event),
)
#respuesta = json.loads(response["Payload"].read().decode())
response = json.loads(response["Payload"].read().decode())
response["body"] = json.loads(response["body"])
pprint(response)