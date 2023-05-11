from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic):
        # auto_offset_reset='earliest',
        # consumer_timeout_ms=1000,
        self.consumer = KafkaConsumer(
            topic,
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            bootstrap_servers=[
                "b-1.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096",
                "b-2.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096",
            ],
            api_version=(2, 6, 2),
            sasl_plain_username="test",
            sasl_plain_password="tb6hNQ3P863GaD42U6X2",
            value_deserializer=lambda x: x.decode(),
        )

    def star_read(self):
        self.receive_message()

    def receive_message(self):
        message_count = 0
        for message in self.consumer:
            message = message.value
            print(f"Message {message_count}: {message}")
            message_count += 1

    def poll_message(self):
        self.consumer.commit_async()
        a = self.consumer.poll()
        return a

    def check(self):
        a = self.consumer.partitions_for_topic("second-topic")
        return a


consumer = Consumer("second-topic")
consumer.star_read()
# consumer.loquequiera()
