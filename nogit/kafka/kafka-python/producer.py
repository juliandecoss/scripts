import logging

from kafka import KafkaProducer


class Producer:
    def __init__(self, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            bootstrap_servers=[
                "b-1.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096",
                "b-2.poc.mqh1l7.c10.kafka.us-west-2.amazonaws.com:9096",
            ],
            api_version=(2, 6, 2),
            sasl_plain_username="test",
            sasl_plain_password="tb6hNQ3P863GaD42U6X2",
            value_serializer=lambda x: (x.encode()),
        )

    def star_write(self, message=None):
        dict_data = message or "envio desde python"
        self.producer.send(
            self.topic,
            value=dict_data,
        )


def main(message):
    logging.info("STARTED")
    producer = Producer("first-topic")
    producer.star_write(message)
    print("MESSAGE SENT")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    message = None
    main(message)
