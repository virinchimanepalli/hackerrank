#!/bin/python3
#hackerrank

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    fm = dict()
    cont = 0
    for i in range(len(ar)):
        if ar[i] in fm.keys():
            fm[ar[i]] += 1
        else:
            fm[ar[i]] = 1
    for i in fm.keys():
        if fm[i] %2 == 0:
            fm[i] = fm[i]/2
            cont = cont + fm[i]
        else:
            fm[i] = (fm[i]-1)/2
            cont = cont + fm[i]
        
    return int(cont)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

#vscode_solution
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
fm = dict()
k = 2
cont = 0
for i in range(len(arr)):
    if arr[i] in fm.keys():
        fm[arr[i]] += 1
    else:
        fm[arr[i]] = 1
for i in fm.keys():
    if fm[i] %2 == 0:
        fm[i] = fm[i]/2
        cont = cont + fm[i]
        # print(cont)
    else:
        fm[i] = (fm[i]-1)/2
        cont = cont + fm[i]

print(int(cont))
print(fm)