"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
可认为硬币数量不限，每种硬币的数量是不限的。
"""
class Solution:
    def coinChange(self, coins,amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i-coin]+1,dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
