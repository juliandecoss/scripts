from json import dumps
from os.path import exists

from client import cognito
from utils import get_device_data_file_path, logger


def confirm_device(helper, response):
    new_device_data = response["NewDeviceMetadata"]
    device_key = new_device_data["DeviceKey"]
    device_group = new_device_data["DeviceGroupKey"]
    device_hashes = helper.generate_device_hashes(device_group, device_key)
    logger("Device password", device_hashes["device_password"])
    confirm_response = cognito.confirm_device(
        AccessToken=response["AccessToken"],
        DeviceKey=device_key,
        DeviceName="Python local testing",
        DeviceSecretVerifierConfig={
            "Salt": device_hashes["salt"],
            "PasswordVerifier": device_hashes["verifier_devices"],
        },
    )
    device_data_file_path = get_device_data_file_path()
    if not exists(device_data_file_path):
        new_device_data["devicePassword"] = device_hashes["device_password"]
        with open(device_data_file_path, "w") as f:
            f.write(dumps(new_device_data))
    logger("Confrim device", confirm_response)
