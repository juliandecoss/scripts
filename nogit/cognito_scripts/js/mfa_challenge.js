const { RespondToAuthChallengeCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { ClientId } = require("./conf.json");
const { getArgs } = require("./utils");
const client = require("./client");


module.exports = response => {
    const { ChallengeName, Session, ChallengeParameters } = response;
    const { USERNAME } = ChallengeParameters;
    if (ChallengeName !== "SOFTWARE_TOKEN_MFA") throw new Error(`ChallengeName: ${ChallengeName}`);
    return client(new RespondToAuthChallengeCommand({
        ClientId,
        ChallengeName,
        Session,
        ChallengeResponses: {
            USERNAME,
            SOFTWARE_TOKEN_MFA_CODE: getArgs().mfaCode,
        },
    }))
        .then(response => {
            console.log(response);
            return response.AuthenticationResult;
        });
};
