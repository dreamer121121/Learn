class Solution:
    def waysToChange(self, n: int):
        coins = [0,1,5,10,25]
        dp = [[0]*(n+1) for _ in range(5)]
        for j in range(5):
            dp[j][0] = 1
        for r in range(1,5):
            for j in range(1,n+1):
                if coins[r] > j:
                    dp[r][j] = dp[r-1][j]
                else:
                    dp[r][j] = dp[r-1][j]+dp[r][j-coins[r]]
        return dp[4][n] % 1000000007
s = Solution()
print(s.waysToChange(900750))
