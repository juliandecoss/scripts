from typing import Optional
from jose import jws, jwt

token="eyJraWQiOiJUeHVEVkdXemx2TWZmcWV5UGdEVzNXQlhSNFN6S2g2amVGY0dmSG9wclA4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI1M2ZiZDA0ZC1kMWE4LTRiOTctOTgyNi1mZjE3MmRkZGQ3Y2UiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfUHFySVZlTk5kIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY3VzdG9tOnBhdGVybmFsX2xhc3RfbmFtZSI6Ikp1YXJleiIsImNvZ25pdG86dXNlcm5hbWUiOiI1M2ZiZDA0ZC1kMWE4LTRiOTctOTgyNi1mZjE3MmRkZGQ3Y2UiLCJhdWQiOiI3amd0ajc5ZGs5N2dpdnNuNG9yNm8yMGQxZiIsImV2ZW50X2lkIjoiMDhmOGI2MDAtMGE2NC00MzJkLThmZmEtZGZhMjY1MmQ3NGMzIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MjMzNDQyMjAsIm5hbWUiOiIhXCLCtyQlJSFcIiUkISIsInBob25lX251bWJlciI6Iis1MjEyMzQ1Njc4OTAiLCJleHAiOjE2MjMzNDc4MjAsImN1c3RvbTptYXRlcm5hbF9sYXN0X25hbWUiOiJUYWdsZSIsImlhdCI6MTYyMzM0NDIyMCwiZW1haWwiOiJqdWd1aUBrb25maW8ubXgifQ.MSoueFdf2fxt8Uxmlz2UqttV6G6P5-zigMGieo6L_hSvqMyv7KSzCgnsVSolrBeP0GR-QHjyQL0da45ZgfOmLTpyvwx-qGC-BKpXvXls_WDxRAqhk7ijoS_sBJ3xllm9soM3W4o4nNEMeWxIbY3bSICwSpISmoeom9CqJpEYd90g8wxoGNrI2mWV9r3DC-Mu5a5J2mxZJauuFf7oLxGCEwm1-pX-Wf5KvZi7FJlDdOsjXH7tBLsnvFUt2H8NdIYhftpivTohSx0WWNUhK3OuEoWmASw1mhQm512u8cBEqnrC_5s3aqQpwWT24IQA5zIsc2MppPzQ-UB6N_RnlSOzEA"
keys = [
        {
            "alg": "RS256",
            "e": "AQAB",
            "kid": "TxuDVGWzlvMffqeyPgDW3WBXR4SzKh6jeFcGfHoprP8=",
            "kty": "RSA",
            "n": "47E5V2UVvG373rjTLim8NJizIfUJ5LQ27PrXoj3uqpGb2UXD1U9IshUUa0mM6PJeXmehugI4KqP2UBsYyJ3dkcEGBPhwIFIGTgNOdJvOEQnACZiYgfmnnDKkmYBJ4fAZi4VWo3zBKcSO4Y5uuy6XA4yMLW4z0S-Dot_AHRYb-ojwHyT1-8TardO3K3--Jedn1DHQrtba64E_N_cIZ4MeTKnIlEJ8cDSNu4M64SkBo3o86FBjp8jf5ERVMY3NE_aNbxul5x0rdGgmJmGFWVoFg3-NlE3dBKg45544OfnL5WLua2OdnmQBofD4lcLxPzn6G1oYf6mS5g_MMnkTDoB_JQ",
            "use": "sig"
        },
        {
            "alg": "RS256",
            "e": "AQAB",
            "kid": "h7EPmmyXBoY/53wI2WP0bD7sdB6TNc/H98qVFJqzYz0=",
            "kty": "RSA",
            "n": "2DEU5Xg1oIOvEAi_MgLo_rkBiTvUDStRrbsJtDyR7CRe5VkjYJbLzQy2rpCwWOfAGnM7pOYAzV1j0CeZVqtAOd3MtC5lSCBuekmJlSYeW4CwhIvwYc2s7xIjh_xKJTtFYanK7zjQhtuTd6ovW1_71bdxQV7sGKZFeNaZnATDu98IflV_0WenFsJ7lG1vCGj7qhBvZmKBiIGe6-2VE7ItFr6qPjZiwC6HkXcyeylMN_0dXsvo1G5oBLKQ3mLr3mvX3aVl3IzIrfDFNEQHbz0MOoHi1nCpG-ZMMgz2bP7U0G1aCA54aowo31KAYBddOESH7qRw2prV0NXnTMKnm0nfdQ",
            "use": "sig"
        }
    ]

def validate_jwt(token):
    try:
        session=jwt.decode(token, keys, algorithms="RS256")

        return session
    except Exception as e:
        return None, e.args
session = validate_jwt(token)
print(session)
print("la chida")

#print(jwt.decode(token,key=None,options={"verify_signature": False}))