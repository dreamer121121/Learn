class Solution():
    def removeElement(self,nums,val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
s = Solution()
print(s.removeElement([3,2,2,3],3))