class Solution:
    def __init__(self):
        self.dir = [(-1,0),(1,0),(0,1),(0,-1)]
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                print("i,j",i,j)
                if self.dfs(i,j,matrix,rows,cols,[],path,[]):
                    return True
        return False
    def dfs(self,cur_i,cur_j,matrix,rows,cols,string,path,sets):
        """
        以当前节点开始的路径是否包含path
        """
        if "".join(string) == path:
            return True
        if cur_i < 0 or cur_i >= rows or cur_j < 0 or cur_j >= cols or (cur_i,cur_j) in sets:
            return False
        sets.append((cur_i,cur_j))
        string.append(matrix[cur_i][cur_j])
        for i in range(len(self.dir)):
            if self.dfs(cur_i+self.dir[i][0],cur_j+self.dir[i][1],matrix,rows,cols,string,path,sets):
                return True
        string.pop()
        sets.pop()
        return False
matrix = [['A','B','C','E'],['S','F','C','S'],['A','D','E','F']]
s = Solution()
print(s.hasPath(matrix,3,4,'ABCCED'))
