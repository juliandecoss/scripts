const { InitiateAuthCommand } = require("@aws-sdk/client-cognito-identity-provider");
const { ClientId, email, password } = require("./conf.json");
const client = require("./client");


module.exports = client(new InitiateAuthCommand({
    ClientId,
    AuthFlow: "USER_PASSWORD_AUTH",
    AuthParameters: {
        USERNAME: email,
        PASSWORD: password,
    }
}))
    .then(async response => {
        console.log(response)
        return response.AuthenticationResult
    });
