#Jumping on the Clouds
# hackerrank
# vscode_solution
ar = [0,0,0,1,0,0,0,0,0,0]
count = 0
i = 0
n = len(ar) -1
while True:
    if i >= n:
        print(count)
        break
    # print(i)
    if i+2 > n:
        count += 1
        print(count)
        break
    if ar[i+2] == 0:
        count +=1
        i = i +2
    else:
        count += 1
        i = i+1



#hackerrank_solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # ar = [0,0,0,0,0,0,1,0,0,1,0]
    count = 0
    i = 0
    n = len(c) -1
    while True:
        if i >= n:
            # print(count)
            return count
            # break
            # return count
        if i+2 > n:
            count +=1
            return count

        if c[i+2] == 0:
            count +=1
            i = i +2
        else:
            count += 1
            i = i+1
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

    