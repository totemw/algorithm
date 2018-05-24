"""
Given an integers array A.
Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1],
calculate B WITHOUT divide operation.
"""

class Solution:
    def productExcludeItself(self, arr):
        if not arr or len(arr) <= 1:
            result = [1]
            return result
        length = len(arr)
        left = [1] * length
        right = [1] * length
        result = []
        for i in range(1, length):
            left[i] = left[i - 1] * arr[i - 1]
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * arr[i + 1]
        for i in range(length):
            res = right[i] * left[i]
            result.append(res)
        return result