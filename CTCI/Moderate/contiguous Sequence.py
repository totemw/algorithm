"""
You are given an array of integers. Find the contiguous sequence
with the largest sum. Return the sum.

compress 2 3 -8 -1 2 4 -2 3
  ->    5 -9 6 -2 3  just let us think this question easily
"""


def getMaxSum(arr):
    maxSum = 0
    curSum = 0
    for i in range(0, len(arr)):
        curSum += arr[i]
        if maxSum < curSum:
            maxSum = curSum
        elif curSum < 0:
            curSum = 0
    return maxSum
