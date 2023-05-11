from boto3 import client


client = client('s3', region_name = 'us-west-2')
def delete_s3_object(bucket: str, key_path: str) -> dict:
    response = client.delete_object(Bucket=bucket, Key=key_path)
    breakpoint()
    response["Body"] = response["Body"].read()
    return response

delete_s3_object("entity-documents-dev","natural-person-req-docs/1492990/sso/refresh_tokens/682712")



""" def delete_s3_object(bucket: str, key_path: str) -> dict:
    response = get_client("s3").delete_object(Bucket=bucket, Key=key_path)
    response["Body"] = response["Body"].read()
    return response

try:
    s3_response = delete_s3_object(
        bucket=f"{ENTITY_DOCUMENTS_BUCKET}-{app.env}", key_path=token_key,
    )
except Exception as e:
    app.logger.info(f"{log_prefix}:s3:delete:refresh:error:{e}")
    raise Exception  # revoke permissions """