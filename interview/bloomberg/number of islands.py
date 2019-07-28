"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input:
11000
11000
00100
00011

Output: 3
"""

# DFS BFS


class Solution(object):
    def DFS(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.DFS(i - 1, j, grid)
        self.DFS(i + 1, j, grid)
        self.DFS(i, j - 1, grid)
        self.DFS(i, j + 1, grid)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(i, j, grid)
                    count += 1

        return count





