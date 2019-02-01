"""
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""
class Solution:
    def isMatch(self, s, pattern):
        n = len(s)
        m = len(pattern)
        f = [[False]*(m + 1) for i in range(n + 1)]
        f[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = (f[i - 1][j - 1] and
                (s[i - 1] == pattern[j - 1]
                 or pattern[j - 1] == '?')
                or (f[i][j - 1] and pattern[j - 1] == '*'))
        return f[n][m]