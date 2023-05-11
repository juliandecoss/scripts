#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: list):
    arr.sort()
    sum = 0
    print(arr)
    for number in arr:
        sum = sum + number 
    max_sum = sum - arr[0]
    min_sum = sum - arr[len(arr)-1]
    print(f"{min_sum} {max_sum}")
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

