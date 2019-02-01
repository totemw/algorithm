"""
Given a string s, cut s into some substrings such that
every substring is a palindrome.
return the minimum cuts needed for a palindrome partitioning of s.
"""

# subproblem: min cut till i (:i)
# dp[i] = min{f[j] + 1} where j < i and str[j : i] is palindrome


class Solution1:
    def minCut(self, s):
        dp = [i for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] == s[i:j][::-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


class Solution2:
    def minCut(self, s):
        dp = [0 for _ in range(len(s) + 1)]
        p = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) + 1):
            dp[i] = len(s) - i
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j - i) < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j + 1], dp[i])
        return dp[0] - 1
