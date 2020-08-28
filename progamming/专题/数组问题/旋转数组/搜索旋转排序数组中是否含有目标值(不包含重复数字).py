class Solution():
    def search(self,nums,target,l,r):
        #依然采用二分法，如何分是关键。
        while l <= r:
            mid = (l+r)>>1
            if nums[mid] == target:
                return True
            if nums[mid]>nums[l]: #之所以只需大于号是因为没有重复数字
                #左边是有序的
                if target>=nums[l] and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid +1
                else:
                    r = mid-1
        return False
s = Solution()
print(s.search([4,5,6,7,0,1,2],target=8,l=0,r=6))