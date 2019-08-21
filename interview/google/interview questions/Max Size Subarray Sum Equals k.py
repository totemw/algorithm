"""
You are given an array of prices of different icecreams.
But your wallet has budget dollars.
Find the length of the longest contiguous subarray whose total price would be equal to your budget.

Example 1:

Input: prices = [2, 5, 7, 8, 9, 18, 2, 2], budget = 14
Output 3
Explanation: 2 + 5 + 7 = 14
"""

def maxSubArrayLen(self, nums, k):
    ans, acc = 0, 0               # answer and the accumulative value of nums
    mp = {0:-1}                 #key is acc value, and value is the index
    for i in range(len(nums)):
        acc += nums[i]
        if acc not in mp:
            mp[acc] = i
        if acc-k in mp:
            ans = max(ans, i-mp[acc-k])
    return ans