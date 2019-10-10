#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    count = 0
    start_count = 0
    for c in s :
        #fptr.write("c is : " + c + '\n')
        if c == 'D' :
            if level <= 0 :
                #fptr.write("is less so start count to 1" + '\n')
                start_count = 1
            level = level - 1
        if c == 'U' :
            level = level + 1
        #fptr.write("level is : " + str(level) + '\n')

        if level == 0 and start_count == 1:
            count = count + 1
            start_count = 0
        #fptr.write("count is : " + str(count) + '\n')       
        #fptr.write("-------------------------------" + '\n')

    #fptr.write(str(count) + '\n' )
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
