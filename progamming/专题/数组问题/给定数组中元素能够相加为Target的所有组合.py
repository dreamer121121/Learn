class Soulution():
    #无重复元素，同一元素在一个组合中可以使用多次，最终解集合中没有重复的组合
    def __init__(self):
        self.reult_all = []

    def combinationSum(self,nums,target):
        nums.sort()
        self.dfs(nums,0,target,[])
        return self.reult_all

    def dfs(self,nums,start,target,result):#用result作为一个栈来存储path
        if sum(result) == target:
            self.reult_all.append(result[:])
            return
        for i in range(start,len(nums)):
            num = nums[i]                      #错误写法：path.append(squarenums[i])
                                               # if sum(path) >target:break
            if sum(result)+num > target:
                break
            result.append(num)
            self.dfs(nums,i,target,result)
            result.pop() #弹出栈顶元素
        return

s = Soulution()
print(s.combinationSum([1,2,3,4,5,6,7,8],9))




