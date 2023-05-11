from os import environ
environ["STAGE"] ="dev"
USER_ADMIN_TYPE = "user_admin"
USER_TYPE = "user"
APP_CLIENTS_REDIS_KEY = "CLIENTS"
APP_CLIENTS_REDIS_EXPIRATION = 28800
AUTHORIZATION_HEADER = "Authorization"
AUTHORIZATION_TYPE_BASIC = "Basic"
AUTHORIZATION_TYPE_BEARER = "Bearer"
COGNITO_ADMIN_DOMAIN_BASE_URL = "COGNITO_ADMIN_DOMAIN"
COGNITO_DOMAIN_BASE_URL = "COGNITO_DOMAIN"
DEFAULT_AUTHENTICATION_SCOPES: list = []
DEFAULT_ERROR_CODE_CLIENT = 1000
DEFAULT_ERROR_CODE_SERVER = 5000
DEFAULT_ERROR_MESSAGE = "Something went wrong"
DEFAULT_REDIS_PREFIX = "PLATFORM:SSO:"
DEFAULT_REDIS_HOST = "localhost"
DEFAULT_REDIS_PORT = 6379
DEFAULT_REQUEST_METADATA_LIFETIME = 15
DEFAULT_SESSION_LIFETIME = 1800
DEFAULT_SSO_PUBLIC_KEYS_LIFETIME = 230400
DEFAULT_SSO_PUBLIC_KEYS_REDIS_KEY = "PUBLIC:KEYS"
DEFAULT_SUCCESSFUL_MESSAGE = "Successful invocation"
DEVICE_MFA_REQUEST_HEADER = "DEVICE_MFA"
EXCEPTION_METADATA_REDIS_KEY = "METADATA:EXCEPTION"
FORGOT_PASSWORD_TOKEN_REDIS_KEY = "FORGOT:PW:TOKEN"
LAMBDA_TASK_ROOT_VAR_NAME = "LAMBDA_TASK_ROOT"
MEXICO_PHONE_COUNTRY_CODE = "+52"
OAUTH_GRANT_TYPE_CLIENT_CREDENTIALS = "client_credentials"
OAUTH_GRANT_TYPE_CLIENT_CREDENTIALS_SCOPES = " ".join(
    ["https://platform.konfio.mx/core/client-admin"]
)
OAUTH_TOKEN_ROUTE = "oauth2/token"
OAUTH_TOKEN_REDIS_KEY = "OAUTH:TOKEN"
REQUEST_METADATA_REDIS_KEY = "REQUEST:METADATA"
SESSION_VAR_SUFFIX = "_SESSION_LIFETIME"
SSM_SSO_BASE_PATH = "platform/sso"
SSM_SSO_CLIENTS_PATH = "clients"
SSO_PUBLIC_KEYS_BASEURL = "https://cognito-idp.us-west-2.amazonaws.com"
SSO_PUBLIC_KEYS_SUFFIX = ".well-known/jwks.json"
TRIGGER_INVALID_RESPONSE_CODE = "InvalidLambdaResponseException"


## App clients ##
APP_CLIENTS = {
    "6n1lss84c3u9ikrio2geln1rig": "gestionix-sso-web-client-dev",
    "37idtvuqst4shha251gsl513fr": "gestionix-sso-web-client-prod",
    "68qdmsiumsgrt99pd2ta1mnupt": "gestionix-duplo-sso-web-client-dev",
    "1apirf17djs9rqhakqrqvkk4k0": "gestionix-duplo-sso-web-client-prod",
    "12cavft59m2iucrr9lpc1cf0vq": "gestionix-totalplay-sso-web-client-dev",
    "238b1brkurvjd3u86iufndsdji": "gestionix-totalplay-sso-web-client-prod",
    "7sc08bamk1lfbr4kneon73jbsv": "gestionix-totalplay-negocios-sso-web-client-dev",
    "4es2i10vvf11n1783qe7q0u5ai": "gestionix-totalplay-negocios-sso-web-client-prod",
    "7nrfcatpn92v76caffk4ihjugq": "gestionix-wingu-sso-web-client-dev",
    "shp27ne0vcshvv4574i3qmksd": "gestionix-wingu-sso-web-client-prod",
    "7o1oqr978s9n0scu05v387qa35": "konfio-sso-android-client-dev",
    "38lefnupktjkprgv5sjg654r8t": "konfio-sso-android-client-prod",
    "246smd2ik7oaqor0h6kum4omk0": "konfio-sso-ios-client-dev",
    "2ml77qopb4umo2oqpktt5er7vs": "konfio-sso-ios-client-prod",
    "2v3tko99u3eiid4hie80udvclk": "konfio-sso-web-client-dev",
    "20dq3jl46movh2fvdugevqnruf": "konfio-sso-web-client-prod",
    "2q6vhk6o6qme3phuocu506aitp": "srpago-sso-core-api-client-dev",
    "39uluq4vrucvld0r02vhja1flh": "srpago-sso-core-api-client-prod",
    "77e41si14jntve704gbtc9374q": "srpago-sandbox-sso-core-api-client-dev",
    "2ubskeili0lagmodla89a0umeq": "srpago-smartpad-sso-core-api-client-dev",
    "2oqcnj2avtqkqa3bavreijvs5f": "srpago-smartpad-sso-core-api-client-prod",
    "5qgke50r0kckm11dh5394riolb": "srpago-staging-sso-core-api-client-dev",
}
DELEGATE_APP_CLIENTS = {
    "2col44s778aeog1a4obbij66co": "platform-core-scope-delegate-client-dev",
    "1k7u80mjla9k79flc40prq4mos": "platform-core-scope-delegate-client-prod",
}
DEPRECATED_APP_CLIENTS = {
    "2a1uak2rhj1kuilvnpg0kdqjn1": "6n1lss84c3u9ikrio2geln1rig",  # gestionix web dev
    "744s1u6qfvress6rsufe4pus2e": "37idtvuqst4shha251gsl513fr",  # gestionix web prod
    "6u958aanrb6csju0tds6dqtspp": "68qdmsiumsgrt99pd2ta1mnupt",  # gestionix duplo dev
    "7ifa9sqp856fbd7lao08ju5pcl": "1apirf17djs9rqhakqrqvkk4k0",  # gestionix duplo prod
    "7m1q0j3q8ndgdvfgurralbu74q": "12cavft59m2iucrr9lpc1cf0vq",  # gestionix total dev
    "7k2daicuuphp9vvh8qa0ca7jdh": "238b1brkurvjd3u86iufndsdji",  # gestionix total prod
    "3njm7n2kmqet4ndl749ij0g3fr": "7nrfcatpn92v76caffk4ihjugq",  # gestionix wingu dev
    "678te75i9fdbs712pipneuhi2m": "shp27ne0vcshvv4574i3qmksd",  # gestionix wingu prod
    "7plq999i25t49jvlekm6hkj3dn": "7o1oqr978s9n0scu05v387qa35",  # konfio android dev
    "646rvattl407bs8hngkeh9qk7e": "38lefnupktjkprgv5sjg654r8t",  # konfio android prod
    "5sbjsi92og2kcr7bknt7iopgha": "246smd2ik7oaqor0h6kum4omk0",  # konfio ios dev
    "2jmdtgc74olv85tr1agm3btoi8": "2ml77qopb4umo2oqpktt5er7vs",  # konfio ios prod
    "7jgtj79dk97givsn4or6o20d1f": "2v3tko99u3eiid4hie80udvclk",  # konfio web dev
    "q3fjsmtdfhan00qf422cgmhs5": "20dq3jl46movh2fvdugevqnruf",  # konfio web prod
}
OAUTH_APP_CLIENTS_SRPAGO_SMARTPAD = {
    "13ufhukfgb2t2tgajtht0f9at4": "srpago-smartpad-oauth-grant-client-dev",
    "7mm1rt0pbhpfhf2cm9t740auq4": "srpago-smartpad-oauth-grant-client-prod",
}
OAUTH_APP_CLIENTS_ADMIN_POOL = {
    "137ff7lhsd5dvs7odetc1jdq6k": "konfio-sso-backoffice-client-dev",
    "6ko293162cd7pt4jfkq1oeoead": "konfio-sso-backoffice-client-prod",
}
OAUTH_APP_CLIENTS = {
    "6ikssc00ottibi8f2dn4g1nfg9": "data-science-oauth-grant-client-dev",
    "7cpqo0d7ru0qjblfdk5i40o5d1": "data-science-oauth-grant-client-prod",
    "18ktnan1fe2lgm196f92rq2t7t": "gestionix-oauth-grant-client-dev",
    "4gqs4rn2beq5krki02givhqc88": "gestionix-oauth-grant-client-prod",
    "mh7m45lopkh30ipqbtfmvg0rd": "konfio-core-oauth-grant-client-dev",
    "g6q8me9an30bj2pq76jl0tbm5": "konfio-core-oauth-grant-client-prod",
    "5n01l2ojtttd6lfjc3i8dloi1g": "machine-learning-oauth-grant-client-dev",
    "2tgo5mof1flb1hs31lmv18se2r": "machine-learning-oauth-grant-client-prod",
    "400lqurvgmrv4aujfg87vllpr6": "salesforce-oauth-grant-client-dev",
    "3v5gol0roti3ujs5vbanvermh1": "salesforce-oauth-grant-client-prod",
    "27jb37a4mtob6r9korp2ktrge3": "srpago-oauth-grant-client-dev",
    "1rc8bh10j07s8tmtuaqle8n9o0": "srpago-oauth-grant-client-prod",
    "6cndvnngb8bsgk0d3jmmiebrbl": "sso-oauth-grant-client-dev",
    "1cng8nfkh1kl3kpcehplo7ege1": "sso-oauth-grant-client-prod",
    **OAUTH_APP_CLIENTS_SRPAGO_SMARTPAD,
    **OAUTH_APP_CLIENTS_ADMIN_POOL,
}
ALL_APP_CLIENTS = {**APP_CLIENTS, **DELEGATE_APP_CLIENTS, **OAUTH_APP_CLIENTS}

def get_app_client_name(client_id: str) -> str:
    if client_id in DEPRECATED_APP_CLIENTS:
        client_id = DEPRECATED_APP_CLIENTS[client_id]
    app_client_name = ALL_APP_CLIENTS.get(client_id)
    if not app_client_name or app_client_name.split("-").pop() != environ["STAGE"]:
        raise Exception("HOla")
    return app_client_name


def get_app_client_data(client_id: str, username: str = "") -> dict:
    splitted_app_client_name = get_app_client_name(client_id).split("-")
    splitted_app_client_name.pop()
    app_client_name = "-".join(e for e in splitted_app_client_name)
    print(app_client_name)
    redis_key = f"{APP_CLIENTS_REDIS_KEY}:{app_client_name}"
    #redis = Redis()
    #app_client_data = redis.get(redis_key)
    if not redis_key:
        ssm_path = f"{SSM_SSO_BASE_PATH}/{SSM_SSO_CLIENTS_PATH}/{app_client_name}"
        print(ssm_path)
        #app_client_data = get_params_values(ssm_path, decrypted=True, recursive=True)
        #redis.set(redis_key, app_client_data, APP_CLIENTS_REDIS_EXPIRATION)
    if username:
        ""
        #app_client_data["secret_hash"] = generate_secret_hash(app_client_data, username)
    return
get_app_client_data("137ff7lhsd5dvs7odetc1jdq6k")