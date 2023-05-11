from csv import writer
from requests import get
from pprint import pprint
cluster_id = "lkc-p7035"
BASIC_TOKEN = "TVlSQVRXSDQ0MkZBUlJJNTpRY1VTTzNHQjNnYWNldndjRFo2TkE5Z3ZzRUFyNDNVQktvSE9PdTBDank4UEhldEMzR3NydnU2YmJ1SGtiZ3pz"
URL = f"https://pkc-pgq85.us-west-2.aws.confluent.cloud:443/kafka/v3/clusters/{cluster_id}/topics"


# API PARA CLUSTER
headers = { 'Authorization': f"Basic {BASIC_TOKEN}" }
response  = get(URL,headers=headers)
topics = response.json()['data']
with open("./nogit/kafka/confluent-api/topics_list.csv", "w") as topics_list_file:
    topics_list_writer = writer(topics_list_file, delimiter=",")
    topics_list_writer.writerow(
            [
            "topic_name",
            "kind",
            "partitions",
            "replication_factor",
            "configs",
            ]
        )
    for topic in topics:
        topic_to_row = []
        topic_to_row.append(topic['topic_name'])
        topic_to_row.append(topic['kind'])
        topic_to_row.append(topic['partitions_count'])
        topic_to_row.append(topic['replication_factor'])
        topic_to_row.append(topic['configs']['related'])
        topics_list_writer.writerow(topic_to_row)
