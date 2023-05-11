import graphene
import requests

key = "NRAK-8NPHBEN3SKA9T9EJZHUDRALQT1U"


class NewRelicQuery(graphene.ObjectType):
    nrql_query = graphene.String()

    @staticmethod
    def resolve_nrql_query(parent, info):
        nrql_query = parent.nrql_query
        query = f"""
        {{
            actor {{
                account(id: 3577612) {{
                    nrql(query: "{nrql_query}") {{
                        results
                    }}
                }}
            }}
        }}
        """
        endpoint = "https://api.newrelic.com/graphql"
        headers = {"API-Key": f"{key}"}
        response = requests.post(endpoint, headers=headers, json={"query": query})
        return response.json()


class Query(graphene.ObjectType):
    nrqlQuery = graphene.Field(NewRelicQuery, nrqlQuery=graphene.String(required=True))

    def resolve_nrqlQuery(self, info, nrqlQuery):
        return NewRelicQuery(nrql_query=nrqlQuery)


schema = graphene.Schema(query=Query)

nrql_query_str = "SELECT count(apm.service.datastore.operation.duration) as 'Database operation Duration', sum(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'Postgres')) FACET `scope` LIMIT max since last month UNTIL this month"

result = schema.execute(
    """
    query($nrqlQuery: String!) {
        nrqlQuery(nrqlQuery: $nrqlQuery) {
            nrql_query
        }
    }
""",
    variables={"nrqlQuery": nrql_query_str},
)

print(result.data)

breakpoint()
