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

def miniMaxSum(arr):
    c=[]
    for i in range(len(arr)):
        a = arr.pop(0)
        c.append(sum(arr))
        arr.append(a)
    
    print(min(c), max(c))
   
        
        
        
        
        
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
