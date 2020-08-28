class Solution:
    def __init__(self):
        self.result = []
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.dfs(root)
        for i in range(len(self.result)):
            if self.result[i] == p:
                if i != len(self.result)-1:
                    return self.result[i+1]
                else:
                    return None
    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.result.append(root)
        self.dfs(root.right)

