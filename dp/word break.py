"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.
"""

# subproblem: str[:i]
# dp[i] = or{dp[j] (j < i) and str[j+1 : i] can be found}
# result: dp[len(str)]


class Solution:
    def wordBreak(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
