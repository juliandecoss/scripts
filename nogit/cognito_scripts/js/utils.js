const date = require("date-and-time");
const CryptoJS = require("crypto-js/core");
const Base64 = require("crypto-js/enc-base64");
const HmacSHA256 = require("crypto-js/hmac-sha256");
const BigInteger = require("./cognito-identity/BigInteger.js");

const { password } = require("./conf.json");


const get_password_claim_signature = (hkdf, firstClaim, secondClaim, secret, timestamp) => {
    const message = CryptoJS.lib.WordArray.create(
        Buffer.concat([
            Buffer.from(firstClaim, "utf8"),
            Buffer.from(secondClaim, "utf8"),
            Buffer.from(secret, "base64"),
            Buffer.from(timestamp, "utf8"),
        ])
    );
    const key = CryptoJS.lib.WordArray.create(hkdf);
    return Base64.stringify(HmacSHA256(message, key));
}

module.exports = get_challenge_response = (helper, params, device_key) => {
    const { SALT, SECRET_BLOCK, SRP_B, USERNAME, DEVICE_KEY } = params;
    const timestamp = date.format(new Date(), "ddd MMM D HH:mm:ss UTC YYYY", true);
    let username = USERNAME;
    let pw = password;
    if (DEVICE_KEY) {
        const { devicePassword } = require("./device_data.json");
        username = DEVICE_KEY;
        pw = devicePassword;
    }
    let signature;
    helper.getPasswordAuthenticationKey(
        username,
        pw,
        new BigInteger(SRP_B, 16),
        new BigInteger(SALT, 16),
        (e, hkdfValue) => signature = get_password_claim_signature(
            hkdfValue, helper.poolName, username, SECRET_BLOCK, timestamp
        ),
    );
    let variable = {
        PASSWORD_CLAIM_SIGNATURE: signature,
        PASSWORD_CLAIM_SECRET_BLOCK: SECRET_BLOCK,
        USERNAME: USERNAME,
        DEVICE_KEY: device_key,
        TIMESTAMP: timestamp,
    };
    console.log(variable)
    return variable
};

module.exports.getArgs = () => {
    const args = process.argv.slice(2);
    let params = {};

    args.forEach(a => {
        const nameValue = a.split("=");
        params[nameValue[0]] = nameValue[1];
    });

    return params;
}