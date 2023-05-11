import requests
import json
from pprint import pprint


def nerdgraph_dashboards(key):
  # GraphQL query to NerdGraph
  query = """
  {
  actor {
    account(id: 3577612) {
      nrql(query: "SELECT count(apm.service.datastore.operation.duration) as 'Database operation Duration', sum(apm.service.datastore.operation.duration) as 'Database operation Calls' FROM Metric WHERE (entity.guid = 'MzU3NzYxMnxBUE18QVBQTElDQVRJT058MTA0NjUzNDU5OA') AND ((operation is not NULL AND datastoreType = 'Postgres')) FACET `scope` LIMIT max since last month UNTIL this month") {
        results
      }
    }
  }
}
  """
  
  # NerdGraph endpoint
  endpoint = "https://api.newrelic.com/graphql"
  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    # convert a JSON into an equivalent python dictionary
    json_dictionary = json.loads(response.content)
    new_relic_data = json_dictionary['data']['actor']['account']['nrql']['results']
    pprint(new_relic_data)
    breakpoint()
    # only interested with the dashboard url
    # url_pdf = json_dictionary["data"]["dashboardCreateSnapshotUrl"]
    # print(url_pdf)

    # replace PDF with PNG, and get the link to download the file
    # url_png = url_pdf[:-3] + "PNG"
    # print(url_png)

    # rename the downloaded file, and save it in the working directory
    # dashboard_response = requests.get(url_png, stream=True)
    # open('dashboard_example.png', 'wb').write(dashboard_response.content)

    # optional - serialize object as a JSON formatted stream
    # json_response = json.dumps(response.json()["data"]["dashboardCreateSnapshotUrl"], indent=2)
    # print(json_response)

  else:
      # raise an error with a HTTP response code
      raise Exception(f'Nerdgraph query failed with a {response.status_code}.')

nerdgraph_dashboards("NRAK-8NPHBEN3SKA9T9EJZHUDRALQT1U")