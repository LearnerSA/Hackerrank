#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import Counter

def allpossible(test_str):
    res = [''.join(sorted(test_str[x:y])) for x, y in combinations(range(len(test_str) + 1), r = 2)]
    return res
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    L=(allpossible(s))
    l1=dict(Counter(L))
    total=0
    for i in l1:
        total += (l1[i]*(l1[i]-1))/2
    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
