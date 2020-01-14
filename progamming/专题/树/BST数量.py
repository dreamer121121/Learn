#本质：卡特兰数，利用动态规划，找到递推关系式。
class Solution():
    def numTrees(self,n):
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]
s = Solution()
s.numTrees(3)
