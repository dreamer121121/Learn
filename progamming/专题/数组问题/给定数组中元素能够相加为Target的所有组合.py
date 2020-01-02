class soulution():
    #无重复元素，同一元素在一个组合中可以使用多次，最终解集合中没有重复的组合
    def __init__(self):
        self.reult_all = []

    def combinationSum(self,nums,target):
        nums.sort()
        self.dfs(nums,0,target,[])

    def dfs(self,nums,start,target,result):#用result作为一个栈来存储path
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






