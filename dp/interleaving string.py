"""
Given three strings: s1, s2, s3,
determine whether s3 is formed by the interleaving of s1 and s2.

Example
For s1 = "aabcc", s2 = "dbbca"
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

# subproblem: s1[:i], s2[:j], s3[:i+j]
# f[i][j] = (s1[i - 1] == s3[i + j - 1] && f[i - 1][j]) ||
#           (s2[j - 1] == s3[i + j - 1] && f[i][j - 1])


class Solution:
    def isInterleave(self, s1, s2, s3):
        len1 = 0 if s1 is None else len(s1)
        len2 = 0 if s2 is None else len(s2)
        len3 = 0 if s3 is None else len(s3)
        if len3 != len1 + len2:
            return False
        dp = [[True] * (1 + len2) for _ in range(1 + len1)]
        for i in range(1, 1 + len1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]
        for i in range(1, 1 + len2):
            dp[0][i] = s2[i - 1] == s3[i - 1] and dp[0][i - 1]
        for i in range(1, 1 + len1):
            for j in range(1, 1 + len2):
                case1 = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                case2 = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                dp[i][j] = case1 or case2
        return dp[-1][-1]