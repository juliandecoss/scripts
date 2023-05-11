const { SetUserMFAPreferenceCommand } = require("@aws-sdk/client-cognito-identity-provider");

const client = require("./client");
const login = require("./user_password")


login.then(response => {
    client(new SetUserMFAPreferenceCommand({
        AccessToken: response.AccessToken,
        SoftwareTokenMfaSettings: {
            Enabled: true,
            PreferredMfa: true,
        },
    }))
        .then(res => console.log(res));
});
