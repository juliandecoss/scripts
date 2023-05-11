from datetime import datetime
from os import environ

from boto3 import resource


def get_dynamo_resource() -> resource:
    return resource("dynamodb",region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com",
                    aws_access_key_id="ASIA5PB6SIHWCBVWBLJV",
                    aws_secret_access_key="E6+GFEmdssilgZvuLypFW7m+ETXaXELtc1VCUze3",
                    aws_session_token="IQoJb3JpZ2luX2VjEPL//////////wEaCXVzLWVhc3QtMSJHMEUCID6HxbL9n5HtPz27eGbqm8P5tH6+DRmxHq/8Oi8B3yHxAiEAyFJK+nnym3J6nKadk8bJzRUyufCSvd1QQM0gHaU5sZMqlgMImv//////////ARAAGgw5MjU2OTY2NzIyMzYiDLwcpB6VQ7pRqnTXBCrqAodyQ4Nnny4lw+2PdA6z3BFWucWzIhABpaB950cRI1AumquHshGXpGDw91vm7+f+vMoF3WUlgyxoNppUymHYr8lZ9JoIVNT9u6u39a69wtfZjvIr0inm+0iGnJYwuCzisTuSc6062bEgr+NQ66ym27XAhhDNnDVVdfvrgnFKP9tLMDLY3rTXLHzli5Dsg2G/rO8RXSEhzDsjRU58zuoRp3yrkP/waJd8tw6hh/tJWHzhfK3MlJ52ojqUkr8qJg7Ziv9aaXSIFY0SsiubdirxYOXlEn46XfwJKhf+zv2AKR54VVgCEo2vgHOWSOvbTOzV9pdNkzIDN06ta50lezgsKBgX2BVB85ekfJsaTXmaeT1UYD0WQnmlWI9v7nvM903D3VAuBMJr/vT3+F15osJwh2/V18MdqRLxA7tIiAaJ5dgBTIbHpHYqkkaBgcNwFNAaOlPhB9UbONSVv4DRttqKtyMyHiAMU50eY6RnMK3w/58GOqYBqCkyh7yUluW3o5ZA2WLnwo5gT6RQ42llihBHZvLWeLKaWJmr9lyHzxSj4pOQ/79B2EzbSPKRcD6xCsBOvgqLGCwflnVY36x+Qr/bD9z4wTq1IDJLCijMkR76qFhyeeL3Sf7KIpEjesOEjzSR0JhnixWHnR9/NOzuCieI4bgOga01pfatKe4nO5XPjqQ/p3DkmDe6dxCCp80Q1LwCLcpMUERw9XTtZg==",
                )


def put_item(table_name: str, values: dict) -> None:
    dynamodb = get_dynamo_resource()
    table = dynamodb.Table(table_name)
    values["CreationDate"] = str(datetime.now()).split(".")[0]
    table.put_item(Item=values)


def get_items(table_name: str) -> list:
    dynamodb = get_dynamo_resource()
    table = dynamodb.Table(table_name)
    return table.scan()["Items"]

data = get_items("t01-use1-events-platform-topics-prd")
breakpoint()