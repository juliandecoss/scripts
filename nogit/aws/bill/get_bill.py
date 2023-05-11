from boto3 import client
# export AWS_ACCESS_KEY_ID="ASIASUBKIF4AXSQBZP6G"
# export AWS_SECRET_ACCESS_KEY="zPHal28mn8BxEQsmkDLK21BbdELHJyyyYA+xpPMH"
# export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjELf//////////wEaCXVzLWVhc3QtMSJGMEQCIBDRJvggygKsdsv7bzppy64zx9+ct7TJZ87lw/Fj7LKjAiBledijgxja50Fm39POGOjJUolEVmv3lpFXmSslpPTlDCqWAwiw//////////8BEAAaDDE4MDQ3NzI0MzEzNyIM9ruRj7bgsuAtYizoKuoCeVV4zR+fyrwPh01B0QYjImdErgGrwG6Rkr4uCzABWAybsGJ9Ze/hksoXvQyaEn9t27lEMfo/ZpFoTmkupqDMgCuBlP1LJqvRdrPapoJHKW4/rNZ+uFU6FXh5gs3VYENeauMN07Ib2tIx1KnXvacZfGBXD5wUsKk9krnvakQ1bljUNpbuNO321g0CEfBJwmOI4ddX6o1GCKZ2VtSsxMnxzoOsWLKAZP5JPbBYMfvGro6zfscTBVAStAVZC6WRyQlTtb1PhrXEb3r6Nn57s5q0GUf47o3/TLdnlocuRE3B5Udg/pibrPXbegkfyZCD3molBYyLmAKJNXMQLQQJrMhaggPaHpmLGaEvlCGNAt3v4u8bQR9FC710M0YKbGm9iq5gvAWmEEXpzAH9zr36PJLEQpAKDQX3qR5uUGDDpx7n5mhFGvOTmASGW7ln7h2oszJLl9SzcVn/0snBroZbr0jhjGQ8AsJ3zYP9+Tcw1pmMogY6pwEZXHXakj4nv0p8UQvKKtgTPpnZY3TgXiX6mPSG2zjV4xPRYvIqze/o4b8N29OyhgANgxQr+rVuekfANcAZQQ6hn25HEWU7RRwlF9fkD4Q8T/+AaPmUYw0hqKdiNGN6CzmRY/jkCOygJYaSdjtw+cILfGevzbGr2RzjQ1W2JnR7Mertd9WO7/59/25wZ4TXs9I7D3FSp7aY3OUKR5usRcB9JMS95kO0kw=="
ce_client = client('ce',
            aws_access_key_id="ASIASUBKIF4AXSQBZP6G",
            aws_secret_access_key="zPHal28mn8BxEQsmkDLK21BbdELHJyyyYA+xpPMH",
            aws_session_token="IQoJb3JpZ2luX2VjELf//////////wEaCXVzLWVhc3QtMSJGMEQCIBDRJvggygKsdsv7bzppy64zx9+ct7TJZ87lw/Fj7LKjAiBledijgxja50Fm39POGOjJUolEVmv3lpFXmSslpPTlDCqWAwiw//////////8BEAAaDDE4MDQ3NzI0MzEzNyIM9ruRj7bgsuAtYizoKuoCeVV4zR+fyrwPh01B0QYjImdErgGrwG6Rkr4uCzABWAybsGJ9Ze/hksoXvQyaEn9t27lEMfo/ZpFoTmkupqDMgCuBlP1LJqvRdrPapoJHKW4/rNZ+uFU6FXh5gs3VYENeauMN07Ib2tIx1KnXvacZfGBXD5wUsKk9krnvakQ1bljUNpbuNO321g0CEfBJwmOI4ddX6o1GCKZ2VtSsxMnxzoOsWLKAZP5JPbBYMfvGro6zfscTBVAStAVZC6WRyQlTtb1PhrXEb3r6Nn57s5q0GUf47o3/TLdnlocuRE3B5Udg/pibrPXbegkfyZCD3molBYyLmAKJNXMQLQQJrMhaggPaHpmLGaEvlCGNAt3v4u8bQR9FC710M0YKbGm9iq5gvAWmEEXpzAH9zr36PJLEQpAKDQX3qR5uUGDDpx7n5mhFGvOTmASGW7ln7h2oszJLl9SzcVn/0snBroZbr0jhjGQ8AsJ3zYP9+Tcw1pmMogY6pwEZXHXakj4nv0p8UQvKKtgTPpnZY3TgXiX6mPSG2zjV4xPRYvIqze/o4b8N29OyhgANgxQr+rVuekfANcAZQQ6hn25HEWU7RRwlF9fkD4Q8T/+AaPmUYw0hqKdiNGN6CzmRY/jkCOygJYaSdjtw+cILfGevzbGr2RzjQ1W2JnR7Mertd9WO7/59/25wZ4TXs9I7D3FSp7aY3OUKR5usRcB9JMS95kO0kw==",   
            )
response = ce_client.get_cost_and_usage_with_resources(
    TimePeriod={
        'Start': '2023-03-01',
        'End': '2023-04-01'
    },
    Granularity='MONTHLY',
    Metrics=["NetUnblendedCost"]
)
breakpoint()