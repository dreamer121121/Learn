#青蛙一侧可跳上1,2,3,4...n级台阶，问跳上一个n级台阶有多少种跳法。
# -*- coding:utf-8 -*-
class Solution():
    def jumpFloorII(self, number):
        #方法一：
        #f(n) = 2**(n-1)
        return 2**(number-1)
    #方法二：
    def jumpFloor2(self,number):
        dp = [0]*(number+1)
        for i in range(1,number+1):
            for j in range(i):
                dp[i] += dp[j]
            dp[i] += 1
        return dp[number]

s = Solution()
print(s.jumpFloorII(4))
print(s.jumpFloor2(4))