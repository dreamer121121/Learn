class Solution:
    def __init__(self):
        self.result = []
    def numSquares(self, n: int) -> int:
        max_num = int(n**0.5)
        squarenums = [num**2 for num in range(1,max_num+1)]
        self.combinationsum(squarenums,n)
        cnt = []
        for each in self.result:
            cnt.append(len(each))
        cnt.sort()
        return cnt[0]
    def combinationsum(self,squarenums,target):#求出列表squarenums中和为target所有组合并将其存入self.resut
        path = []
        squarenums.sort()
        self.dfs(squarenums,0,target,path)
    def dfs(self,squarenums,start,target,path):
        if sum(path) == target:
            self.result.append(path[:])
            return
        for i in range(start,len(squarenums)):
            if sum(path)+squarenums[i] > target:
                break
            path.append(squarenums[i])
            self.dfs(squarenums,i,target,path)
            path.pop()
        return