class soulution():
    def __init__(self):
        self.result_all = []

    def combinationSum(self,nums,target):
        nums.sort()
        print("排好序：",nums)
        self.dfs(nums,0,target,[])

    def dfs(self,nums,start,target,result):#用result作为一个栈来存储path
        if sum(result) == target:
            self.result_all.append(result[:])
            return
        for i in range(start,len(nums)):
            num = nums[i]
            if sum(result)+num > target:
                break

            #进行剪枝操作
            if i > start and nums[i-1] == nums[i]: #若i=start则不进行剪枝
                continue

            result.append(num)
            self.dfs(nums,i+1,target,result)
            result.pop() #弹出栈顶元素
        return


s = soulution()
s.combinationSum([10,2,7,6,1,5,2,4],8)
print(s.result_all)

