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

def timeConversion(s:str):
    # Write your code here
    time = s.split(":")
    if "AM" in time[2]:
        if time[0] == "12":
            time[0] = "00"
        time[2] = time[2].replace("AM","")
        s =":".join(time)
    else:
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
        time[2] = time[2].replace("PM","")
        s =":".join(time)
    print(s)
if __name__ == '__main__':

    s = "07:05:45PM"

    timeConversion(s)