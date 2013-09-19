#HW1-II.py
#Program by Valerie Lambert

"""
Given lists C and S of n and m integers in the range [0,k], we must 
preprocess C and S in O(m+n+k) time so that, given a and b in [0,k],
we can output the number of integers in C in the range [a.b] and the
number of integers in S in [a.b] in O(1) time.
"""

import random

def createarrays():
    arr1 = []
    arr2 = []
    p = 50
    k = 100
    n = random.randint(0,k+1)
    m = random.randint(n,k+1)
    arr1 = [random.randint(0,p) for i in range(0,n)]
    arr2 = [random.randint(0,p) for i in range(0,m)]
    return arr1, arr2


def main():
    for i in range(0,5):
        arr1, arr2 = createarrays()
        print(arr1)
        print(arr2)
        print("Arrays created. Preprossesing...")

main()
