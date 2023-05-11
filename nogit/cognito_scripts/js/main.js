const fs = require('fs');

const srpa_auth = require("./sra_initiate_auth");
const confirmDevice = require("./confirm_device");


deviceDataFile = "./device_data.json"
device_key = null
if (fs.existsSync(deviceDataFile)) {
    const { DeviceKey } = require(deviceDataFile);
    device_key = DeviceKey
}

srpa_auth(device_key)
    .then(auth_response => {
        let { response, helper } = auth_response;
        if (response && response.NewDeviceMetadata) return confirmDevice(response, helper).then(res => res)
        return response || auth_response;
    });
