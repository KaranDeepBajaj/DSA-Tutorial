#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

lis=[]
lis

def dynamicArray(n, queries):
    arr=[[] for _ in range(n)]
    answer=[]
    lastAnswer = 0
    for i in queries:
        query,x,y=i
        if query==1:
            idx=(x^lastAnswer)%n
            arr[idx].append(y)
        elif query==2:
            idx=(x^lastAnswer)%n
            lastAnswer=arr[idx][y%len(arr[idx])]
            answer.append(lastAnswer)
    return answer

dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])