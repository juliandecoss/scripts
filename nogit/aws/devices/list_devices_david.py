from botocore.exceptions import ClientError
from dateutil import tz
import boto3

DEV = "us-west-2_PqrIVeNNd"
PROD = "us-west-2_VODHRFn7A"
def list_devices(username: dict) -> dict:
    try:
        client = boto3.client('cognito-idp', region_name = 'us-west-2')
        list_devices = client.admin_list_devices(
            UserPoolId=DEV, Username=username
        )
        remembered = []
        for device in list_devices["Devices"]:
            for attributes in device["DeviceAttributes"]:
                if attributes["Name"] == "device_name":
                    device_name = attributes["Value"]
                elif attributes["Name"] == "dev:device_remembered_status":
                    device_status = attributes["Value"]
            last_seen = device["DeviceLastAuthenticatedDate"]
            device_key = device["DeviceKey"]
            last_seen_date = last_seen.astimezone(tz.tzlocal())
            if device_status == "remembered":
                remembered.append(
                    {
                        "remember_status": device_status,
                        "device_name": device_name,
                        "last_seen_date": last_seen_date.ctime(),
                        "device_key":device_key
                    }
                )
        return {"list_devices": remembered}
    except ClientError as e:
        print(e)
        raise Exception
    
todo=list_devices("9a13b67d-456d-40e9-91d1-d5cde0395c4c")
breakpoint()