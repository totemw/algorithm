"""
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Note
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
"""

# sub problem: f(x, y) -> last line
# f(x, y) = min{f(x+1, y), f(x+1. y+1)} + triangle[x][y]


class Solution:
    def minimumPath(self, triangle):
        if len(triangle) == 0:
            return 0
        dp = triangle[-1][:]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

    # which is equal to
    def minimumPath(self, triangle):
        return reduce(lambda a, b:[min(a[i], a[i+1]) + n for i, n in enumerate(b)], triangle[::-1])[0]
