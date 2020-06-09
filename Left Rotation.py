# Arrays: Left Rotation
#vscode solution
ar = [1,2,3,4,5]
def leftRotation(ar,d,ln):
    l_index = ln -1
    # ln = len(ar)
    k = []
    # d = 4 #where d is number of rotations
    dl = ln - d
    lnth = ln - dl
    # print(lnth)
    for i in range(d,ln):
        k.append(ar[i])

    for i in range(lnth):
        k.append(ar[i])
    listToStr = ' '.join(map(str, k))
    # print(k)
    return listToStr
d = int(input("enter number of rotations " ))
ln =  len(ar)
print(leftRotation(ar,d,ln))
#hackerrank
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    l_index = len(a) -1
    ln = len(a)
    k = []
    # d = 4
    dl = ln - d
    lnth = ln - dl
    for i in range(d,ln):
        k.append(a[i])
        # print(k[i])
    for i in range(lnth):
        k.append(a[i])
    listtostr = ' '.join(map(str, k))
    print(k)
    return listtostr
        # return (k[i],end = " ")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(''.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


