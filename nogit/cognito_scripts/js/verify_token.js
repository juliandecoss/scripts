const { VerifySoftwareTokenCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { FriendlyDeviceName } = require("./conf.json");
const client = require("./client");
const { getArgs } = require("./utils")


module.exports = response => client(new VerifySoftwareTokenCommand({
    AccessToken: response.AccessToken,
    FriendlyDeviceName,
    UserCode: getArgs().secretCode,
}))
    .then(res => console.log(res));
