"""
A child is running up a staircase with n steps and can hop either
1 step. 2 steps or 3 steps
"""

def countWays(n):
    dp = [1 for _ in range(n + 1)]
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]
