num_of_candles = int(input())
candles = list(map(int, (input().split())))

max_counts = 0
max_length = 0

while num_of_candles:
    num_of_candles-=1

    if max_length < candles[num_of_candles]:
        max_counts = 1
        max_length = candles[num_of_candles]
    elif max_length == candles[num_of_candles]:
        max_counts+=1

print(max_counts)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    num_of_candles = len(candles)

    max_counts = 0
    max_length = 0

    while num_of_candles:
        num_of_candles-=1

        if max_length < candles[num_of_candles]:
            max_counts = 1
            max_length = candles[num_of_candles]
        elif max_length == candles[num_of_candles]:
            max_counts+=1

    return max_counts
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
