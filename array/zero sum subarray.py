"""
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.
"""

# hash table
class Solution:
    def subarraySum(self, arr):
        hash = {0 : -1}
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum == 0:
                return [0, i]
            if sum in hash:
                return [hash[sum] + 1, i]
            hash[sum] = i
        return