"""
robot at the upper left corner of the grid with r rows and c columns
robot can only move right and down
some cells cannot be stepped on
"""


def grtPath(maze):
    m = len(maze)
    n = len(maze[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j]
            elif i and j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

