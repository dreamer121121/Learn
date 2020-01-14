#本题的关键是找到递推关系：
#c0 = 0,c1 = 1,c2 = 2 c3 = 3 当n > 2时：c(n) = c(n-1) + c(n-2)
class Solution():
    def jumpFloor(self, number):
        #递归法
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

    def jumpFloor2(self,number):
        #动态规划
        dp = [0]*(number+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for j in range(3,number+1):
            dp[j] = dp[j-1]+dp[j-2]
        return dp[number]

s = Solution()
print(s.jumpFloor2(3))