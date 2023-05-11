const { AssociateSoftwareTokenCommand } = require("@aws-sdk/client-cognito-identity-provider");

const client = require("./client");
const login = require("./user_password");


login.then(response => client(new AssociateSoftwareTokenCommand({
    AccessToken: response.AccessToken,
}))
    .then(res => console.log(res))
);
