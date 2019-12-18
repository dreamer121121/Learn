class solution():
    def __init__(self):
        self.result = 0

    def find_index(self,nums,target,start,end):
        if start == end:
            return
        mid = (start+end)//2
        mid_num = nums[mid]
        if target == mid_num:
            self.result = mid
            return
        elif target > mid_num:
            self.result = mid+1
            self.find_index(nums,target,mid+1,end)
        elif target < mid_num:
            self.result = mid-1
            self.find_index(nums,target,start,mid)


    def findtargetindex(self,nums,target):
        self.find_index(nums,target,0,len(nums)-1)
        return self.result

s = solution()
print(s.findtargetindex([1,3,5,7,8,10,15,23],9))
# findtargetindex([1,3,5,7],7)
