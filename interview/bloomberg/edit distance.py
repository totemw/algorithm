"""
Given two words word1 and word2, find the minimum number of steps required
to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

# subproblem: word1[:i], word2[:j]


class Solution:
    def minDistance(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = i
        for i in range(m):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
        return dp[-1][-1]