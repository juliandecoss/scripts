import boto3

from pprint import pprint
from time import time_ns
times = []
for _ in range(10):
    start_time = time_ns()
    client = boto3.client('cognito-idp', region_name='us-west-2')
    paginator = client.get_paginator('list_users').paginate(UserPoolId="us-west-2_PqrIVeNNd", Filter="phone_number = \"+519611230729\"", PaginationConfig={"MaxItems": 1}).search("Users")
    #if next((user for user in paginator), None): raise Exception("Uh uh uh! You didn't say the magic word! Uh uh uh! Uh uh uh!")
    #next((user for user in paginator), None) 
    if paginator : print("si hay users")
    end_time = (time_ns() - start_time) // 1000000
    times.append(end_time)
    print(end_time)
print(times,sum(times))
print(sum(times)/len(times), "ms")
#29.2ms
#669.2