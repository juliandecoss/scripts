#for manage errors 

# elif msg.error():
#     if msg.error().code() == KafkaError._PARTITION_EOF:
#         log = f"Topic: {msg.topic()} in partition: {msg.partition()} reached end at offset {msg.offset()}"
#     elif msg.error():
#         raise KafkaException(msg.error())