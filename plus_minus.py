#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p=0
    n1=0
    z=0
    for i in range(len(arr)):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n1+=1
        else:
            z+=1
        
    print("{:.6f}".format(p/n), "\n", "{:.6f}".format(n1/n), "\n", "{:.6f}".format(z/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# Input 
# 6
# -4 3 -9 0 4 1

# Ouput 
# 0.500000
# 0.333333
# 0.166667
