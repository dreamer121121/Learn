nums = [4, 3, 2, 3, 5, 2, 1]
class Solution:
    def canPartitionKSubsets(self, nums,k):
        if not nums:
            return False
        target,mod= divmod(sum(nums),k)
        if mod:
            return False
        used = set() #用于记录已经使用过的元素
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        def dfs(k,start = 0,tmpSum = 0):#从start开始找到K个使tmpSum=target，返回bool值，相信能实现
            #递归终止条件
            if tmpSum == target: #找到了一个满足条件的组合再从头重新找
                return dfs(k-1,0,0)
            if k == 1:
                return True
            for i in range(start,len(nums)):
                if i not in used and nums[i]+tmpSum <= target:
                    used.add(i)
                    if dfs(k,i+1,nums[i]+tmpSum):
                        return True
                    used.pop()
            return False
        return dfs(k,0,0)
    
s = Solution()
print(s.canPartitionKSubsets(nums,4))




