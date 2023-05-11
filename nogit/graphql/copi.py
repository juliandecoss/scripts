import json
from pprint import pprint

import requests
from graphql_query import Argument, Field, Operation, Query

KEY = "NRAK-8NPHBEN3SKA9T9EJZHUDRALQT1U"
query = "SELECT count(apm.service.datastore.operation.duration) as 'Database operation Duration', sum(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'Postgres')) FACET `scope` LIMIT max since last month UNTIL this month"
actor = Query(
    name="actor",
    fields=[
        Field(
            name="account",
            arguments=[Argument(name="id", value=3577612)],
            fields=[
                Field(
                    name="nrql",
                    arguments=[Argument(name="query", value=f'"{query}"')],
                    fields=["results"],
                )
            ],
        )
    ],
)
hero = Query(
    name="account",
    arguments=[Argument(name="id", value=3577612)],
    fields=[
        Field(
            name="nrql",
            arguments=[Argument(name="query", value=f'"{query}"')],
            fields=["results"],
        )
    ],
)
operation = Operation(type="", queries=[actor])
print(operation.render())
endpoint = "https://api.newrelic.com/graphql"
headers = {"API-Key": f"{KEY}"}
response = requests.post(endpoint, headers=headers, json={"query": operation.render()})

if response.status_code == 200:
    json_dictionary = json.loads(response.content)
    rds_information = json_dictionary["data"]["actor"]["account"]["nrql"]["results"]
    new_rds_info = []
    for info in rds_information:
        info['Scope'] = info.pop('scope')
        new_rds_info.append(info)
    rds_information = new_rds_info
    pprint(rds_information)
    breakpoint()
