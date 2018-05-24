"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Have you met this question in a real interview? Yes
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.
"""

# subproblem str1[:i], str2[:j]


class Solution:
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
        for i in range(1, 1 + len(B)):
            for j in range(1, 1 + len(A)):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]