class soulution():
    def __init__(self):
        self.reult_all = []

    def combinationSum(self,nums,target):
        nums.sort()
        self.dfs(nums,0,target,[])

    def dfs(self,nums,start,target,result):
        if sum(result) == target:
            self.reult_all.append(result[:])
            return
        for i in range(start,len(nums)):
            num = nums[i]
            if sum(result)+num > target:
                break
            result.append(num)
            self.dfs(nums,i,target,result)
            result.pop() #弹出栈顶元素
        return






