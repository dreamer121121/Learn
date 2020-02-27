class Solution():
    def maxsubArray(self,nums):
        #暴力法O(N2)
        max_sum=-float('inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum > max_sum:
                    max_sum = sum
                else:
                    continue
        return max_sum
    def maxsubArray2(self,nums,l,r):
        #方法一：分治法 O(logN)
        if l >= r:
            return nums[l]
        mid = (l+r)//2
        left_sum = self.maxsubArray(nums,l,mid)
        right_sum = self.maxsubArray(nums,mid+1,r)
        cross_sum = self.crosssum(nums,mid,l,r)
        return max(left_sum,right_sum,cross_sum)

    def crosssum(self,nums,mid,l,r):
        max_left = -float('inf')
        sum = 0
        for i in range(mid,l-1,-1):
            sum += nums[i]
            if sum > max_left:
                max_left = sum
            else:
                continue
        max_right = -float('inf')
        sum_r = 0
        for i in range(mid+1,r+1):
            sum_r += nums[i]
            if sum_r > max_right:
                max_right = sum_r
            else:
                continue
        return max_left + max_right

    def maxsubArray3(self,nums):
        #动态规划O(N)
        dp = []
        dp.append(nums[0])
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i])) #关键找到此递推关系式
            #当前这个位置为止的最大子序和为上一个位置为止的最大自序和加上当前位置的值，与当前位置的值相比大者。
            
        return max(dp)

s = Solution()
print(s.maxsubArray([-2,1,-3,4,-1,2,1,-5,4],0,7))
print(s.maxsubArray3([-2,1,-3,4,-1,2,1,-5,4]))
