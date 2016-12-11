#!/bin/python3

# question url: https://www.hackerrank.com/challenges/circular-array-rotation

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]



for a0 in range(q):
    m = int(input().strip())
    print(a[(m-k)% len(a)])


    '''
    This is how you do the rotation using

    rotate by 2 elements
    1 2 3 4 5 6
    2 1 6 5 4 3
    3 4 5 6 1 2
    '''