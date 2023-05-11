import json
from pprint import pprint

from requests import post
from graphql_query import Argument, Field, Operation, Query
KEY = "NRAK-8NPHBEN3SKA9T9EJZHUDRALQT1U"
NR_ACCOUNT_ID = 3577612

def run_query_by_graphql(query:str):
    actor = Query(
    name="actor",
    fields=[
        Field(
            name="account",
            arguments=[Argument(name="id", value=NR_ACCOUNT_ID)],
            fields=[
                Field(
                    name="nrql",
                    arguments=[Argument(name="query", value=f'"{query}"')],
                    fields=["results"],
                )
            ],
        )
    ],)
    operation = Operation(type="", queries=[actor])
    endpoint = "https://api.newrelic.com/graphql"
    headers = {"API-Key": f"{KEY}"}
    response = post(endpoint, headers=headers, json={"query": operation.render()})

    if response.status_code == 200:
        json_dictionary = json.loads(response.content)
        query_information = json_dictionary["data"]["actor"]["account"]["nrql"]["results"]
        return query_information
    print(response.reason)
    return