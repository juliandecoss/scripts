#!/usr/bin/env bash

#===============================================================================
# SET AUTH DOMAIN
#===============================================================================
AUTH_DOMAIN="sso-konfio-dev.auth.us-west-2.amazoncognito.com"

#===============================================================================
# AUTH CODE/IMPLICIT GRANTS, WITHOUT PKCE, WITHOUT CLIENT SECRET
#===============================================================================

## Set constants ##
CLIENT_ID="2col44s778aeog1a4obbij66co"
RESPONSE_TYPE="code"
#RESPONSE_TYPE="token"
REDIRECT_URI="https://dev.konfio.mx/mi/dashboard/negocio/staff/agregars"
SCOPE="openid"

USERNAME="jugui@gmail.com"
PASSWORD="test123"

## Get CSRF token and LOGIN URL from /oauth2/authorize endpoint ##
curl_response="$(
    curl
     -qv "https://${AUTH_DOMAIN}/oauth2/authorize?response_type=${RESPONSE_TYPE}&client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${SCOPE}" 2>&1
)"
echo "https://${AUTH_DOMAIN}/oauth2/authorize?response_type=${RESPONSE_TYPE}&client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&scope=${SCOPE}"
curl_redirect="$(printf "%s" "$curl_response" \
                    | awk '/^< Location: / {
                        gsub(/\r/, ""); # Remove carriage returns
                        print $3;       # Print redirect URL
                    }')"
echo $curl_redirect
csrf_token="$(printf "%s" "$curl_response" \
                   | awk '/^< Set-Cookie:/ {
                       gsub(/^XSRF-TOKEN=|;$/, "", $3); # Remove cookie name and semi-colon
                       print $3;                        # Print cookie value
                    }')"
echo $csrf_token
## Get auth code or tokens from /login endpoint ##
curl_response="$(
    curl -qv "$curl_redirect" \
        -H "Cookie: XSRF-TOKEN=${csrf_token}; Path=/; Secure; HttpOnly" \
        -d "_csrf=${csrf_token}" \
        -d "username=${USERNAME}" \
        -d "password=${PASSWORD}" 2>&1
)"

curl_redirect="$(printf "%s" "$curl_response" \
                    | awk '/^< Location: / {
                        gsub(/\r/, ""); # Remove carriage returns
                        print $3;       # Print redirect URL
                    }')"

auth_code="$(printf "%s" "$curl_redirect" \
                | awk '{
                    sub(/.*code=/, ""); # Remove everything before auth code
                    print;              # Print auth code
                }')"
