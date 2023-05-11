const { RespondToAuthChallengeCommand } = require("@aws-sdk/client-cognito-identity-provider");
const AuthenticationHelper = require("./cognito-identity/AuthenticationHelper");
const { ClientId } = require("./conf.json");
const get_challenge_response = require("./utils")
const client = require("./client");

const date = require("date-and-time");

//module.exports = (helper, device_key, response) => {
    //const { ChallengeName, ChallengeParameters, Session } = response;
    //if (ChallengeName !== "DEVICE_PASSWORD_VERIFIER") throw new Error(`ChallengeName: ${ChallengeName}`);
    let helper = new AuthenticationHelper("-Vfxs5RNW")
    let device_key = "us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d"
    let ChallengeParameters={
        PASSWORD_CLAIM_SIGNATURE: 'P/bN0iD3uyMTJqMMy3mTQNJYXfPj9UvgWQ0ssdJedtQ=',
        PASSWORD_CLAIM_SECRET_BLOCK: '3YFoXmI82guGQg97oWjm9+zBuhZw1wChNdkb2XYdbV3dqWu44hv8iJ+5RlZ7hbPs1Gt6ZhR6mg5SxL/DuqvTxZ+77EATTGNuEYNkn19hGMWgOWUMyL+Nk43H6rv2aNcXqN/LhkwwSvqg30bwPLBiOnJS4Wq8gca7zKLGP6LFUs4P+T19/bcKeQNGb9Mn1UHsNTEW7nQfUZElvWN1hqM4RL+7Jw2MTzh4eKLcQy0mAcCYT3MI7IcKi41loVbN4CuHhB7AqSlX+NR64/A8ZMWoXXg60WMSHqn7Ku4ttaSALH2ekMLaV1Zxk2rhmIqeSruX5xQwKlYj/9qqJLtr8fCVgwQH5RVFNHC00Pc5bFjYEW65tqnn+igWns5hRpT0s6BoGb4xrKMnAeH7fBjKmKF0mIiIApjgud6V/toRJqoEX38P20vZ3l8tljfSjMysl3NyQGRGnuE/NopfohanqKDE2cbyvnUGOzEHFy/sSEHtCBD774SrM170yVfkq4867mqUqWDLSYY/BUIvQ8st9JtpdZIBq+4TkWWXM8fM3iMThe+kMzDBQ3INwBLPiboh1zhjimiZriohRbQnmiEFxMlShHpvIPfdKOCKyG75gyDnrpxv0Dh2ioDUuty2NvH2NhSFjZVmTWU1svSyWnBIrwDIj9s+x4mRvWiAZexkSt+Hxyv2H4AxOIHk9kGRPWBrrA6uRmwD8qnb2iClI6Sf8kWGFYIcC9xXf5juaPMLi0qH5FYvNumt8BrkT52qQDz4hmxdsA8qF3z/lVJA+vDmKyyodBfvcEeXlc+dFjg+G01U2ymwNRPXHAXk80SjSw0j1Em5hHWJkSsckM3MzQOXy+GL7DKQfmKK/H+ostz1KCYF+ioy1CHRABd571a77gXRIPnL/GxZBJ0pBN4BpuKZz107dbaoov/rRqcsxbJZtQy4EAy26AVkOJFVt1yEUKVhX4hXvwAR1XckSgs2K7DqW4KMWpaX18/4HeU86ahqlSSGm8/skwr+O2cCqEewjNeh7Xs2QTaI4iQEBcd0cp3MA7ZmBnbBH5N3wNrwP6iwAkDaNUdK5ulomFOTawrBbr0dYeR7SdLAnPezDayZfx8ayKEofS27rAMwWH8eyD64vMZY1FFo1a+HRtNBwrx9I+GjfyHolvfD192j/Dbu9zFUFwfI0LyMQd2cJh6lNb+0yuBk29JS3CzlvY28EviPTUSz7PlXnxWVQgQn3bSK7L6QgatKfeZLg03U/4/T+HbcycwrGGKWYoVVBttJ2jokGbzZtxHCurbWO3hmAYtyeh8Kkq0bKtQorgNIKYfZGgWMHSY8mivK9BNQEhFO8+ZAxl7Oq0ol3ZLrLIl7QYLkHh75xhiSZLE6f9qpuxNqgkMHfP9+AHSVd5GrQwMW2OVFHYBH/Pa0Fhy9lFCYOHEcoM6hb3+awhttGMI2GPlBg6qZWllPY8Ac5o6jYwoDGT5wi3leYgIzc7I9wt9y0xc0YaaUevKJm/V4BieGmbgMyJF/C9qiPfT789dkF261YOgyE5ILRelcl8oYGCurwmWO9e5SO1pcfhqd7zPGAO+rON3B5mo73Abl3KDWKVJe0ah2yNJJyg/w0mGZhwtJCwJqTaZWiPQSMa46O2cR/Gts6KnEUVrTuo8BU/4v7aTJoY0FhWgqLiqj3m8S29c+0pMwgBDZRo6Fna7hMLOzxZ65sUZY5zKMvvtidwJaUQyp7CJZ',
        USERNAME: '23daf9dd-117d-48f0-9a41-3ed5fd6a74b0',
        DEVICE_KEY: 'us-west-2_6edc4131-cafc-4ed6-b425-8c7ad47eed7d',
        TIMESTAMP: 'Fri Aug 6 17:34:17 UTC 2021'
      }
    return client(new RespondToAuthChallengeCommand({
        ClientId,
        ChallengeName:"DEVICE_PASSWORD_VERIFIER",
        Session:"AYABeBY920Nzjk7orhZ92E6pUL8AHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLXdlc3QtMjowMTU3MzY3MjcxOTg6a2V5LzI5OTFhNGE5LTM5YTAtNDQ0Mi04MWU4LWRkYjY4NTllMTg2MQC4AQIBAHiLcRcG62Mb19KUM6qQUoajwNOF_-4FakXKLIP1RcBYjQGw9obhmbORECju6RqJemKkAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMhyWKw9egR4MdvJW6AgEQgDsmCXf1QxtOzrzzQkQorr60ghGhNud_83v5USkeTKQUyNvEuI1ddZnw2TZdX5eJ34PHLcdPXIxSmgA8XQIAAAAADAAAEAAAAAAAAAAAAAAAAAAtprN7IsfmbUIAL_yASeHR_____wAAAAEAAAAAAAAAAAAAAAEAAADn11OLvLRKfqZ0AK3L1AWgKQiGHqtOFeTTFQwZOprCERhT3xwQ1Srz4IZokTzQqvGzO26PrYPV4i00jqQWHXIo-fX864FlzUQ0CES8sPgx-50tmi8S1kEpZnn4oorSUOxadHQqekK5knXP71KQSJIpPla2zKV0Fh3lZ7Nnjw4DzpEwNtyxQddh4eiQxGeZX9PQ4TuZDR8yv5i-UdOK1AbscVnSrfSay51NTJym0G5uig54RqCBvXDsXfrkMvFtd98fYCmq4Hi0Y2NWq1E2Rwow0GPD2YHAh-eVA0pefPdf04SHki5a8TS3IV4bu_XJIVXlXSUP92RYNg",
        ChallengeResponses: ChallengeParameters,
    }))
        .then(response => {
            console.log(response);
            return response;
        });
//};
