a = [10,9,2,5,3,7,101,18]
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * (len(nums)+1) #缓存结果
        dp[0] = 0
        for i in range(1,len(nums)+1):
            tmp = 0
            for j in range(i):
                if dp[j] > tmp and nums[j-1] < nums[i-1]:
                    tmp = dp[j]
                    dp[i] = tmp +1
        print(dp)
        dp.sort()
        return dp[-1]
s = Solution()
print(s.lengthOfLIS(a))