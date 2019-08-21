"""
Say you have an array for
which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example
Given an example [3,2,3,1,2], return 1
"""


class Solution1:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        low = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            maxprofit = max(maxprofit, prices[i] - low)
        return maxprofit

"""
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""


class Solution2:
    def maxProfit(self, prices):
        if len(prices) <= 1 or prices is None:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit


"""
Design an algorithm to find the maximum profit.
You may complete at most two transactions.
"""

# profit for [1 : i] + [i + 1 : n]

class Solution3:
    def maxProfit(self, prices):
        if len(prices) <= 1 or prices is None:
            return 0
        n = len(prices)
        profit = 0
        profit_front = [0] * n
        valley = prices[0]
        for i in range(1, n):
            profit_front[i] = max(profit_front[i - 1], prices[i] - valley)
            valley = min(valley, prices[i])
        profit_back = [0] * n
        peak = prices[-1]
        for i in range(n - 2, -1, -1):
            profit_back[i] = max(profit_back[i + 1], peak - prices[i])
            peak = max(peak, prices[i])
        for i in range(n):
            profit = max(profit, profit_back[i] + profit_front[i])
        return profit


"""
Design an algorithm to find the maximum profit.
You may complete at most k transactions.
"""
import sys

class Solution4:
    def maxProfit(self, k, prices):
        if len(prices) <= 1 or prices is None:
            return 0
        n = len(prices)
        fm = 0
        km = 0
        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                fm += profit
                km += 1
        if k >= km:
            return fm
        else:
            dp = [0 for _ in range(n)]
            for i in range(1, k + 1):
                balance = -sys.maxsize
                prev = dp[0]
                for j in range(1, n):
                    balance = max(balance, prev - prices[j - 1])
                    prev = dp[j]
                    dp[j] = max(dp[j - 1], balance + prices[j])
        return dp[-1]

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        dp[:i][:j] means i times and prices[:j] (first jth prices)
        dp[i][j] = max(dp[i][j-1] (not sell), 
                       max(dp[i-1][k] + prices[j-1] - prices[k])
                            for k in range (0, j-1)
                       )
        """
        import sys

        dp = [[0 for _ in range(len(prices) + 1)] for _ in range(k + 1)]
        print(dp)
        for i in range (1, k + 1):
            tmpMax = -sys.maxsize
            for j in range(2, len(prices) + 1):
                # tmpMax = max(tmpMax, dp[i-1][j] - prices[j])
                # dp[i][j] = max(dp[i][j], prices[j-1] + tmpMax)
                for k in range(j - 1):
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + prices[j-1] - prices[k])
                dp[i][j] = max(dp[i][j], dp[i][j-1])
        print(dp)