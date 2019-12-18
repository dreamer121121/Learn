class Solution():
    def nextPermutation(self,nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                exchange_index = i
                for j in range(i,len(nums)):
                    if nums[j]>nums[i-1]:
                        exchange_index = j
                nums[i-1],nums[exchange_index] = nums[exchange_index],nums[i-1]
                nums[i:] = nums[len(nums)-1:i-1:-1] #利用反向切片进行反转
                return nums
            else:
                continue
        nums.sort()
        return nums
s = Solution()
print(s.nextPermutation([2,3,1]))
