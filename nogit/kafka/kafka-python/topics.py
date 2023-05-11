from kafka.admin import KafkaAdminClient, NewTopic

breakpoint()
admin_client = KafkaAdminClient(
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    bootstrap_servers=[
        "b-1-public.micropoc.9nylnx.c10.kafka.us-west-2.amazonaws.com:9196"
    ],
    api_version=(2, 6, 2),
    sasl_plain_username="test",
    sasl_plain_password="tb6hNQ3P863GaD42U6X2",
)

topic_list = []
topic_list.append(
    NewTopic(name="topic_partido", num_partitions=1, replication_factor=2)
)
admin_client.create_topics(new_topics=topic_list, validate_only=False)
breakpoint()
