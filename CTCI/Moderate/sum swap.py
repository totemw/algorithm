"""
Given two arrays of integers, find a pair of values
that you can swap to give the two arrays the same sum

the problem reduces to finding a pair of values that have a particular difference
we can throw all the elements in B into a hash table
and iterate through A
"""


def findSwapValues(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    diff = (sum1 - sum2) / 2
    h = {}
    for num in arr2:
        h[num] = True
    for num in arr1:
        d = num - diff
        if d in h:
            return num, d
    return False
