"""
Given a (m x n) grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.
Note
You can only move either down or right at any point in time.
"""

# subproblem: min-path form (0, 0) to (x, y)
# f[x][y] =  grid[x][y] + min{f[x - 1][y], f[x][y - 1]}


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # initialize the basic value for dp
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]