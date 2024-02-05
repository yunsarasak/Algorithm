#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    row_length = len(arr)
    row_index = row_length
    sum_from_bottom_right = 0
    sum_from_bottom_left = 0

    #print(row_length)

    while row_index:
        row_index -= 1
        col_index = row_index
        sum_from_bottom_right += arr[row_index][col_index]
        #print("sum_from_bottom_right %d added"%arr[row_index][col_index])
        sum_from_bottom_left += arr[row_index][row_length - col_index -1]
        #print("sum_from_bottom_left %d added"%arr[row_index][row_length - col_index -1])

    answer = sum_from_bottom_left - sum_from_bottom_right
    if answer < 0:
        answer *= -1
        
    return answer

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #fptr = open(1, 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
