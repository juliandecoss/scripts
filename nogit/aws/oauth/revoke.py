from os import environ
from requests import post
from urllib.parse import urlencode
from base64 import b64encode

environ["COGNITO_DOMAIN_BASE_URL"] = "https://sso-konfio-dev.auth.us-west-2.amazoncognito.com"
def cognito_oauth_revoke(payload: dict, headers: dict) -> None:
    base_url = environ.get("COGNITO_DOMAIN_BASE_URL", "")
    headers.update(
        {
            "Content-Type": "application/x-www-form-urlencoded",
           # "Accept": "application/json",
        }
    )
    response = post(
        f"{base_url}/oauth2/revoke", headers=headers, data=urlencode(payload)
    )
    breakpoint()
    if response.status_code != 200:
        breakpoint()
        raise Exception
    return
client_id = "2col44s778aeog1a4obbij66co"
app_client = {"secret":"1qrorupfvpq0igrfiiq0tg5b5obp0bn6s76607rqt717ote9515k","id":"2col44s778aeog1a4obbij66co"}
credentials = b64encode(
    f'{app_client["id"]}:{app_client["secret"]}'.encode()
).decode()
headers = {"Authorization": f"Basic {credentials}"}
token = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.X-ZGfkISk04B2-C1zUuDVq5Hifmy1SUzbyYVJjK31PPRsSDfVKwKqe6yX0FEr7WTLr4O5WAPDXDH2q0znrgj7zEZIau9j5G-6lWMUqGJajNrOjMHBHSXR_E0VRZm_rWkhy8kMNFBC1EwJUIoA5mqOqLbqtHNZOuv4OUzfL7DvAXTLjmTPP-rFj9TxYk5KuphedusKS359RBo77OKZJ1UGpRS6D6MaCtFWd6e60IXllZ3wLz_BeQjsgxjHrt82zknj_x9E0uupKlcCtjVXh6c4Zku7E84yzvmAX-sm0LZqVM0O8bk4Au-rnUHjzXJfgi1Qp2KGHMpLMrYHBUOGSdK3g.Y2FJvy972g2WYpZR.klERmk6d8I2oI0k_m0wd7JoUz9XIQJaL9AzbKJdsNXfAgZ73SIdcCPBD5whiWH0d_2STjOkzUK_ww0MUU8ahSnrtKlrikjGI_MnJExitAjeGQQ_uSlf6k3cDp0Lv3IYcKcyazzaWRpM5Bvuyj8FERX-yo0SE_pDS6MY_8G1YZ5ApulpoKCWPZJXG6sr6hYPUkLUmrLhYLGmB57DnD75YmFMkePm89S6aWoOo8aoojKfa6K4fp7GrctOSZ_i1mcNLbxmIx5tCmdNl8YkkJzHVLDUM3M0sw9mqpIFuKPOIKZrZmcoH02gg_JA_nDIs6kDTLORI2ld4Kn_b0ue2dVicKOPdgXE3Truu4S78J68icXv6ZHI6FmUDNrH1zwNnCmcxKkJqSH2-To09b56pc9w8W2TDw_aR0iizurj1Qoi2_DBLQ8sSQRU-cwAtGxOlCTNGdLvhkMaXbUkFtCm54I5sHTxpCwBzsC-aGgbqSembWUZt1XpPUedLKLX34ZTbd1oNyHKVVtnqxhmEnmEuNSuKS7h9J-pOXEKbctVZg0mw7pkt6IWLpNOmThksD7G4wO0Q2JBSrDYibQZSNNf-s02x6PLQtNeA_I1dTiRloHtPnHKY9npTNdsE6a8eDnn11WuXlt7SpaCBlNVDRTk4pehC9YG7M_4_ymWvwl-KwLr45sQSrh69lDCzZPEWQKgdcAq1umHpXTC-qqrq-WF9dIPGVeSW08Hi8Fy1_flFLZz0OHIjF1Dgs9CwPvTPdkvtASfo_JUAFu_bTLTOUqB8AU3KtQu9Cn48LXEyScnIdT-bxNlV6qbGDQ99Kw_lxbASuwQqNe0yZMj3P5WKb4TmYOfjpxgzqx18rJmFBVi-qV2c-2BJQRo2thMlakeTT6GmmrvuwDsKiXsbgKRvHoWLY0-xobBPd_vKpEoOis6hrJHKxRbSYT6tBu-_0T8ULnbGPguzr4OhbYqJgZ_ZuxTBq643MmYuX6R_cS8BfYOaj75-rUkCeU1lSjbxhYNw62UNT93SFzTRhQfhEqD_dh7Q0Z2KqrtvSoeRI9iVpuXVq4HPXxN09a2h0BBJAY1qTY_92Tt1LxGxTkKkj-6MBi_mgONXIXfSuAvcavZWodPjziEIJARqBDlXqhauPv1u_KPn5Q3QMj_c06vLvahVlhranNRf1C4lllNdMf4BDyALPQEqyN6VS6hLk-mcAJxA-xYAG86OGNLO2dkIFyvpRwqLeh9RCysdST4FVirPaC6su_HQWrO-AwNFPXHLmiC6EAwCrfUnE15QyupnzoGwCdiDj3_RBMJ61CnwJuOj_EoSXFaWyzfqswSWT1hT91skpuwrxdn7GrHjLj4fOyn0rhP4SowDSeWVIc_ZVJ9ES5RAhiUmUkHnyOOfnvSf_akqv5uc9hkIgCJZ6tX1fZrKm_03yw.tbnLP7g7_K7NB2Pewq0Hfg"
res = cognito_oauth_revoke({"token": token},{})
