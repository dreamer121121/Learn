class Solution():
    def removeDuplicates(self,nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
s = Solution()
print(s.removeDuplicates([1,1,2]))