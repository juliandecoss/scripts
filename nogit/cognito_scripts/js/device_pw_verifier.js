const { RespondToAuthChallengeCommand } = require("@aws-sdk/client-cognito-identity-provider");

const { ClientId } = require("./conf.json");
const get_challenge_response = require("./utils")
const client = require("./client");


module.exports = (helper, device_key, response) => {
    const { ChallengeName, ChallengeParameters, Session } = response;
    if (ChallengeName !== "DEVICE_PASSWORD_VERIFIER") throw new Error(`ChallengeName: ${ChallengeName}`);
    //console.log(Session)
    get_challenge_response(helper, ChallengeParameters, device_key)
    /* return client(new RespondToAuthChallengeCommand({
        ClientId,
        ChallengeName,
        Session,
        ChallengeResponses: ,
        
    }))
        .then(response => {
            console.log(response);
            return response;
        }); */
};
