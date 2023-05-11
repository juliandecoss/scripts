import boto3
from pprint import pprint
from csv import reader, writer

#317 topicos de SNS
client = boto3.client(
        "sns",
        aws_access_key_id="ASIASUBKIF4AVJX27XVE",
        aws_secret_access_key="DyIlnkBZT2RzO4HzuORqKVbj+Vw7hJXIr18igxL/",
        aws_session_token="IQoJb3JpZ2luX2VjEL///////////wEaCXVzLWVhc3QtMSJHMEUCIQC8oJoiLq7fp2JeBvJMS+MUe7jZlry1Qv60Sg5FvxGiyQIgVJX3US4R80o+pEeE1VVTXn20LYVtuhMMy2stf4uqpvsqlQMIyP//////////ARAAGgwxODA0NzcyNDMxMzciDBsWTyO4WIXAGP7a/CrpApVTucrF4h13air1nJ81hCcyg8XqL1aNUVboOGCgp46WZT86cDy7qJxF28wk7nrTwm7pzvtrcxU2LRzWrz4TapM+Is/I4avqkWkdpNZfGaCJqgrRIHW03fO/tcdEf1jOA1Tsj8d25mVycBa/DETpE5KHtUcGwuUIRQVD1x6pe9rHzBqnrj3u5B8+mFFETn5lKaU5xL6yVAUZUJ2TCMwew0RAOJoy+lmmc1/gbSpQ55az3/NCZBYAquIBg3IO+irxSWd30JYCwjZFzWaZqpc4z1Eds6klEji6D44LAC0MNHK24smxucR9MTPjSs7KDtX4+r+j5S7wyv/gU/LyoBFIhzD4IEfNpMdHmSRAn/eqAi+DLROjktobb3L8cO8Xf5UtcMEppOfsMKTWV5Ncaj2wEmbvMX/BWol22LgP5bzRZnUmG9+K9ClDCnhxIglLmAsCOX/z81nmEPpefIeJZ1zh2QSEFPz80XrGV70w4sv6mwY6pgEgmaUoLikjvO67b7aKoFvo21g8g53V3P7ArykTQtIHrhRWp3++/M49Exz06w4yperuJ852vIMY8NleUu0epb5qLxqhul58mVAlJOVnCxh+jS+jVH9Bx+3Nsu/T4Bxk78rb1K0hcf6HSGNQrWnG1b3whbIlXl48RZ+UcR2TiYjmbtdCkvuO+wBvsRZPl37dhhg/PMfOb9yf5k+rjogFGbFwWoZFdJde"
)
response:dict = client.list_topics()
topicos = len(response['Topics'])
with open("sns_topics.csv", 'w') as f:
    write = writer(f, delimiter=',')
    row_to_write = []
    for topic in response["Topics"]:
        topic = topic['TopicArn']
        row_to_write.append(topic.split(":")[-1])
        row_to_write.append(topic)
        write.writerow(row_to_write)
        row_to_write = []
    while 1:
        token = response.get('NextToken',{})
        if token:
            response:dict = client.list_topics(NextToken=token)
            topicos += len(response['Topics'])
            for topic in response["Topics"]:
                topic = topic['TopicArn']
                row_to_write.append(topic.split(":")[-1])
                row_to_write.append(topic)
                write.writerow(row_to_write)
                row_to_write = []
        else:
            break
print(topicos)