const { CognitoIdentityProviderClient } = require("@aws-sdk/client-cognito-identity-provider");

const { region } = require("./conf.json");


const client = new CognitoIdentityProviderClient({ region });

module.exports = command => client
    .send(command)
    .then(data => data)
    .catch(error => console.error(error));
