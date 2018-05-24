"""
Given an nonnegative integer array, find a subarray where
the sum of numbers is k. Your code should return the index
of the first number and the index of the last number.
"""

# hash table - similar method
def maxSubArrayLen(A, k):
    hs = {0: -1}
    sum = 0
    for i in range(len(A)):
        # if A[i] == 0:
        #     return [i, i]
        sum += A[i]
        if sum - k in hs:
            return [hs[sum - k] + 1, i]
        hs[sum] = i
    return