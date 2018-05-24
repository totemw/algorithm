"""
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).
"""

# subproblem: unique paths from (0, 0) to (x, y)
# dp[x][y] = dp[x - 1][y] + dp[x][y - 1]


class Solution1:
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            dp = [[1]]
        elif m == 1:
            dp = [[1 for _ in range(n)]]
        elif n == 1:
            dp = [[1] for _ in range(m)]
        else:
            dp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(0, n):
                dp[0][i] = 1
            for i in range(0, m):
                dp[i][0] = 1
            for i in range(m):
                for j in range(n):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            return dp[-1][-1]



"""
Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note
m and n will be at most 100.
"""


class Solution2:
    def uniquePathsWithObstacles(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif j != 0 and i == 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
