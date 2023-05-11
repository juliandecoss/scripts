const fs = require('fs');

const { ConfirmDeviceCommand } = require("@aws-sdk/client-cognito-identity-provider");

const client = require("./client");
const srpa_auth = require("./sra_initiate_auth");


module.exports = (auth_result, helper) => {
    const newDeviceMetadata = auth_result.NewDeviceMetadata
    const deviceDataFile = "./device_data.json"
    const device_key = newDeviceMetadata.DeviceKey;
    // generateHashDevice receives deviceKey instead of username?
    helper.generateHashDevice(newDeviceMetadata.DeviceGroupKey, device_key, (e, n) => { });
    client(new ConfirmDeviceCommand({
        AccessToken: auth_result.AccessToken,
        DeviceKey: device_key,
        DeviceName: "Nodejs local testing",
        DeviceSecretVerifierConfig: {
            Salt: Buffer.from(helper.SaltToHashDevices, 'hex').toString('base64'),
            PasswordVerifier: Buffer.from(helper.verifierDevices, 'hex').toString('base64'),
        },
    }))
        .then(r => {
            newDeviceMetadata.devicePassword = helper.randomPassword;
            if (!fs.existsSync(deviceDataFile)) fs.writeFile(deviceDataFile, JSON.stringify(newDeviceMetadata), e => { })
            console.log(r);
            srpa_auth(device_key)
                .then(auth_response => {
                    console.log(auth_response);
                    return auth_response.AuthenticationResult;
                });
        });
}
