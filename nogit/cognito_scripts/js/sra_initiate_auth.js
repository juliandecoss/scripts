const { InitiateAuthCommand, RespondToAuthChallengeCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { ClientId, email, userPoolId } = require("./conf.json");
const get_challenge_response = require("./utils")
const client = require("./client");
const AuthenticationHelper = require("./cognito-identity/AuthenticationHelper");
const mfaChallenge = require("./mfa_challenge");
const deviceSrpChallenge = require("./device_srp_challenge");


const userPoolName = userPoolId.split("_")[1]
const helper = new AuthenticationHelper(userPoolName);
const srp_a = helper.largeAValue.toString(16);
console.log(`SRP_A: ${srp_a}`);

module.exports = device_key => client(new InitiateAuthCommand({
    ClientId,
    AuthFlow: "USER_SRP_AUTH",
    AuthParameters: {
        USERNAME: email,
        SRP_A: srp_a,
        DEVICE_KEY: device_key,
    },
}))
    .then(response => {
        console.log(response);
        const { ChallengeName, Session, ChallengeParameters } = response;
        if (ChallengeName !== "PASSWORD_VERIFIER") throw new Error(`ChallengeName: ${ChallengeName}`);
        console.log("===========================> SESSION <=============================================")
        console.log(Session)
        console.log("===========================>   END     <=============================================")
        return client(new RespondToAuthChallengeCommand({
            ClientId,
            ChallengeName,
            Session,
            ChallengeResponses: get_challenge_response(helper, ChallengeParameters, device_key),
        }))
            .then(response => {
                console.log(response);
                response.ChallengeParameters.USERNAME = ChallengeParameters.USERNAME
                if (!device_key && response.ChallengeName == "SOFTWARE_TOKEN_MFA") {
                    return mfaChallenge(response).then(res => {
                        return { response: res, helper }
                    })
                }
                else if (response.ChallengeName == "DEVICE_SRP_AUTH") {
                    return deviceSrpChallenge(response, device_key).then(res => res);
                }
                return { response, helper };
            });
    });
