from os import environ

environ['STAGE'] = 'prod'
groups = ["admin"]
ADMIN_GROUPS = ["admin","user-admin"]
is_admin = True if any([key in groups for key in ADMIN_GROUPS]) else False

ALL_APP_CLIENTS = {
    "nk17dd1pdkk3bevsvdtpcd4vs": "konfio-backoffice-sso-admin-client-prod",
    "2cs85dtq1ntnjnrbtt8bau7me5": "konfio-backoffice-sso-admin-client-dev",
}
def get_app_client_name(client_id: str) -> str:
    app_client_name = ALL_APP_CLIENTS.get(client_id)
    if not app_client_name or app_client_name.split("-").pop() != environ["STAGE"]:
        raise Exception
    return app_client_name


def get_app_client_data(client_id: str, username: str = "") -> dict:
    splitted_app_client_name = get_app_client_name(client_id).split("-")
    splitted_app_client_name.pop()
    app_client_name = "-".join(e for e in splitted_app_client_name)
    print(app_client_name)

get_app_client_data("nk17dd1pdkk3bevsvdtpcd4vs")
environ['STAGE'] = 'dev'
get_app_client_data("2cs85dtq1ntnjnrbtt8bau7me5")