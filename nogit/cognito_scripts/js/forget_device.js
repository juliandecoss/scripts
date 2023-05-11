const fs = require('fs');

const { ForgetDeviceCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { DeviceKey } = require("./device_data.json");
const client = require("./client");
const srpa_auth = require("./sra_initiate_auth")


srpa_auth(null)
    .then(auth_response => client(new ForgetDeviceCommand({
        AccessToken: auth_response.response.AccessToken,
        DeviceKey,
    }))
        .then(res => {
            console.log(res);
            fs.unlink("./device_data.json", e => { })
        })
    );
