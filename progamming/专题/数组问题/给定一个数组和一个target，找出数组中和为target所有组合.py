#题目：
# 输入：给定一个数组，数组中无重复元素，给定一个target值
# 输出：和为target的所有组合
# 注意：数组中的数可以重复使用，输出的结果里没有重复的组合

#思路：
#输入：[1,2,3,4,5,9,8],target=3,
#输出：[[...],[...],[...],...]
class Solution():
    def __init__(self):
        self.result = []
    def combinationSum(self,nums,target): #题目给的原始函数
        nums.sort()
        path = []
        self.dfs(nums,0,target,path)
        return self.result

    def dfs(self,nums,start,target,path):
        #函数定义：将nums[i]到nums[len(nums)-1]为根节点的和为target的组合存入到self.result数组中
        if sum(path) == target:
            self.result.append(path[:])
            return
        for i in range(start,len(nums)):
            num = nums[i]
            if sum(path)+num > target:
                return
            path.append(num)
            self.dfs(nums,i,target,path)
            path.pop()

s = Solution()
print(s.combinationSum([1,2,3,4,5,6,7,8],9))



