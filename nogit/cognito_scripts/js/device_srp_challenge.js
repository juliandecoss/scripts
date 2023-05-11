const { RespondToAuthChallengeCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { ClientId } = require("./conf.json");
const client = require("./client");
const AuthenticationHelper = require("./cognito-identity/AuthenticationHelper");
const devicePasswordChallenge = require("./device_pw_verifier");


module.exports = (response, device_key) => {
    const { ChallengeName, Session, ChallengeParameters } = response;
    if (ChallengeName !== "DEVICE_SRP_AUTH") throw new Error(`ChallengeName: ${ChallengeName}`);
    const { DeviceGroupKey } = require("./device_data.json");
    const { USERNAME } = ChallengeParameters;
    const helper = new AuthenticationHelper(DeviceGroupKey);
    const srp_a = helper.largeAValue.toString(16);
    console.log(`SRP_A: ${srp_a}`);
    return client(new RespondToAuthChallengeCommand({
        ClientId,
        ChallengeName,
        Session,
        ChallengeResponses: {
            USERNAME,
            DEVICE_KEY: device_key,
            SRP_A: srp_a,
        },
    }))
        .then(response => {
            console.log(response);
            return devicePasswordChallenge(helper, device_key, response).then(res => res);;
        });
};
