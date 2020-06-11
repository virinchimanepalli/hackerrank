#vscode_solution
# Sparse Arrays problem
# There is a collection of input strings and a collection of query strings.
# For each query string, determine how many times it occurs in the list of input strings.

def array(st,qr):
    fm = dict()
    k = []
    for i in range(len(st)):
        if st[i] in fm.keys():
            # pass
            fm[st[i]] +=1
        else:
            fm[st[i]] = 1
    for i in range(len(qr)):
        if qr[i] in fm.keys():
            k.append(fm[qr[i]])
        else:
            k.append(0)
    return k

st = ['ab','ab','abc','bc']
qr = ['ab','abc','bc']
print(array(st,qr))

#hackerrank rolution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    st = strings
    qr = queries
    
    fm = dict()
    k = []
    for i in range(len(st)):
        if st[i] in fm.keys():
            # pass
            fm[st[i]] +=1
        else:
            fm[st[i]] = 1
    for i in range(len(qr)):
        if qr[i] in fm.keys():
            k.append(fm[qr[i]])
        else:
            k.append(0)
    return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
