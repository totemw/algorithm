"""
Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string
which is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""

# subproblem: s[:i] t[:j]


class Solution:
    def numDistinct(self, S, T):
        if S is None or T is None:
            return 0
        if len(S) < len(T):
            return 0
        if len(T) == 0:
            return 1
        dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
        for i, Si in enumerate(S):
            for j, Tj in enumerate(T):
                if Si == Tj:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[-1][-1]