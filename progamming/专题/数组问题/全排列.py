#经典的回溯问题
#全排列问题可以看成是经典的回溯问题，
class Solution:
    def __init__(self):
        self.result = []
    def permute(self, nums):
        path = []
        self.length = len(nums)
        self.dfs(nums,path)
        return self.result
    def dfs(self,nums,path):#函数定义：求nums的全排列并存入path中
        if len(path) == self.length:
            print(path)
            self.result.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            new_nums = nums[:i]+nums[i+1:]
            self.dfs(new_nums,path)
            path.pop()
        return
s = Solution()
print(s.permute([1,2,3]))