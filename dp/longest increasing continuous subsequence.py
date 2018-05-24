"""
Give you an integer array (index from 0 to n-1, where n is the size of this array)
find the longest increasing continuous subsequence in this array.
(The definition of the longest increasing continuous subsequence here
 can be from right to left or from left to right)
"""


# dp[:i]


class Solution1:
    def longestSubsequence(self, arr):
        if arr is None or len(arr) == 0:
            return 0
        start = 0
        licsMax = 1
        ascending = False
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                if not ascending:
                    ascending = True
                    start = i - 1
            elif arr[i - 1] > arr[i]:
                if ascending:
                    ascending = False
                    start = i - 1
            else:
                start = i
            licsMax = max(licsMax, i - start + 1)
        return licsMax


sol = Solution1()
print sol.longestSubsequence([1, 1, 1, 1])

"""
Give you an integer matrix (with row size n, column size m)find the longest
increasing continuous subsequence in this matrix. (The definition of the longest 
increasing continuous subsequence here can start at any row or column and 
go up/down/right/left any direction)
"""


# dp[i][j]


class Solution2:
    def longestSubsequence(self, arr):
        DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        if arr is None or len(arr) == 0:
            return 0
        self.n = len(arr)
        self.m = len(arr[0])
        self.matrix = [[0] * self.b for _ in range(self.n)]
        for i in xrange(self.n):
            for j in xrange(self.m):
                self.search(arr, i, j)

        return max(max(row) for row in self.matrix)

    def search(self, A, x, y):
        if self.matrix[x][y] != 0:
            return self.matrix[x][y]

        longest = 1
        for dx, dy in self.DIRECTIONS:
            if x + dx < 0 or x + dx >= self.n:
                continue
            if y + dy < 0 or y + dy >= self.m:
                continue
            if A[x][y] >= A[x + dx][y + dy]:
                continue
            longest = max(longest, self.search(A, x + dx, y + dy) + 1)
        self.matrix[x][y] = longest
        return self.matrix[x][y]
