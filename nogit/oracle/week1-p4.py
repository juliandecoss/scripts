#!/bin/python3

from array import array
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

def breakingRecords(scores:list)->array:
    min_record = 0
    max_record = 0
    break_max_record = 0
    break_min_record = 0
    timer = 0
    for score in scores:
        timer += 1
        if timer>1:
            if score < min_record:
                min_record = score
                break_min_record += 1
            elif score > max_record:
                max_record = score
                break_max_record += 1
        else:
            min_record = score
            max_record = score
    return [break_max_record,break_min_record]
if __name__ == '__main__':

    scores = [10,5,20,20,4,5,2,25,1]

    print(breakingRecords(scores))
    max_points = scores[0]
    less_points = scores[0]
    counter_max = 0
    counter_less = 0
    for pos,record in enumerate(scores):
        if pos != len(scores) -1:
            next_record = scores[pos+1]
            if next_record > max_points:
                max_points = next_record
                counter_max += 1
            elif next_record < less_points:
                less_points = next_record
                counter_less += 1
    print([counter_max, counter_less])

