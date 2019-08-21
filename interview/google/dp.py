"""
question could be dp
find true/false, min/max value, all possible solutions

"""

"""
non repeat subset sum
dp(i,j) = dp(i-1, j) + dp(i - 1, j - s[i-1]))
"""
def change(self, amount, coins):
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= coins[i - 1]:
                dp[i][j] += dp[i - 1][j - coins[i - 1]]
    print(dp[-1][-1])

"""
repeat subset sum
dp(i,j) = dp(i-1, j) + dp(i, j - s[i-1]))
"""
def change(self, amount, coins):
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= coins[i - 1]:
                dp[i][j] += dp[i][j - coins[i - 1]]
    print(dp[-1][-1])