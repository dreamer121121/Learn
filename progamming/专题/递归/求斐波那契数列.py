#关键递归式：c0=0,c1 = 1,c(n) = c(n-1) + c(n-2)
class Solution():
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)
    def Fibonacci2(self,n):
        #动态规划
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for j in range(2,n+1):
            dp[j] = dp[j-1] + dp[j-2]
        return dp[n]
s = Solution()
print(s.Fibonacci(6))