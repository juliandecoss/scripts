import boto3
from typing import Optional
from botocore.client import Config
from json import dumps, loads
AWS_REGION = 'us-west-2'
from time import time
from pprint import pprint

def invoke_lambda(function_name: str,message: dict,qualifier: Optional[str] = "$LATEST",synchronous: bool = False,timeout: int = 60,) -> dict:
    start_time = time()
    invocation_type = "Event"
    if synchronous:
        invocation_type = "RequestResponse"
    lambda_client = boto3.client(
        "lambda",
        region_name=AWS_REGION,
        aws_access_key_id="AKIASUBKIF4AXZIAEW5J", aws_secret_access_key="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",
        config=Config(
            signature_version="s3v4", connect_timeout=timeout, read_timeout=timeout,
        ),
    )
    payload = dumps(message)
    byte_payload = payload.encode()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType=invocation_type,  # can use 'DryRun' for testing
        Payload=byte_payload,
        Qualifier=qualifier,
    )

    elapsed = time() - start_time
    print(f"aws:lambda:{elapsed}")

    return response
scopes_completos = "openid profile https://platform.konfio.mx/core/profile.admin https://platform.konfio.mx/core/enterprise.admin https://platform.konfio.mx/core/loan.admin https://platform.konfio.mx/core/cards.admin https://platform.konfio.mx/core/kopay.admin https://platform.konfio.mx/core/payments.admin https://platform.konfio.mx/core/inventory.admin https://platform.konfio.mx/core/reporting.admin"
query_parameters = {
        "response_type": "code",
        "client_id": "2col44s778aeog1a4obbij66co",
        "redirect_uri":"https://dev.konfio.mx/mi/dashboard/negocio/staff/agregar",                
        "scope": scopes_completos,
        "state": "state",
    }
qualifier = "dev"
lambda_event = {
    "path":"/authorize",
    "headers": {"PLATFORM-ORIGIN": "LOCAL"},
    "requestContext": {
        "stage": qualifier,
        "path": "/authorize",
    },
    "queryStringParameters": query_parameters,
    "body": "",
}
lambda_result = invoke_lambda(
    function_name='sso-oauth-token',
    message=lambda_event,
    qualifier=qualifier,
    synchronous=True,
)
response = loads(lambda_result["Payload"].read().decode())
pprint(response)
response["body"] = loads(response["body"])
pprint(response)
pprint(response["headers"])