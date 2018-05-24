"""
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
For [4, 2, 4, 5, 3, 7], the LIS is [4, 4, 5, 7], return 4
"""

# subproblem: the length of increasing subsequence ended with i
# dp[i] = max{dp[j] + 1}


class Solution:
    def longestIncreasigSubsequence(self, arr):
        if not arr:
            return 0
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[j] <= arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)