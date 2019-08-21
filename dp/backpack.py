"""
Given n items with size Ai, an integer m denotes the size of a backpack.
How full you can fill this backpack?

If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5],
so that the max size we can fill this backpack is 10
"""

class Solution1:
    def backpack(self, arr, m):
        length = len(arr)
        dp = [[0 for _ in range(m + 1)] for _ in range(length + 1)]

        # initialize
        for i in range(length + 1):
            dp[i][0] = 0

        for i in range(m + 1):
            dp[0][i] = 0  # false

        for i in range(1, length + 1, 1):
            for j in range(1, m + 1, 1):
                if arr[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], arr[i - 1] + dp[i - 1][j - arr[i - 1]])
        print(dp)
        return dp[-1][-1]



"""
Given n items with size Ai and value Vi, and a backpack with size m. 
What's the maximum value can you put into the backpack?
"""


class Solution2:
    def backPackII(self, arr, values, m):
        dp = [0 for _ in range(m + 1)]
        for i in range(len(arr)):
            for j in range(m, arr[i] - 1, -1):
                dp[j] = max(dp[j], values[i] + dp[j - arr[i]])
        return dp[m]