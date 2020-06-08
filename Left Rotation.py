# Arrays: Left Rotation
#vscode solution
ar = [41 ,73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97,  58, 1, 86, 58, 26, 10, 86, 51]
l_index = len(ar) -1
ln = len(ar)
k = []
d = 10 #where d is number of rotations
dl = ln - d
lnth = ln - dl
print(lnth)
for i in range(d,ln):
    k.append(ar[i])

for i in range(lnth):
    k.append(ar[i])
listToStr = ''.join(map(str, k))
print(k)
print(listToStr)

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


