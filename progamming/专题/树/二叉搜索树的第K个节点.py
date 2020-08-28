from binarytree import Node
root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(13)
print(root)

# class Solution():
#     # 返回对应节点TreeNode
#     def __init__(self):
#         self.nodes = []
#     def KthNode(self, pRoot, k):
#         self.midorder(pRoot)
#         return self.nodes[k-1]
#     def midorder(self,root):
#         if not root:
#             return
#         self.midorder(root.left)
#         self.nodes.append(root)
#         self.midorder(root.right)

class Solution:
    def dfs(self,root):
        """
        返回当前节点为根节点的树的节点数量
        :param root:
        :return:
        """
        if not root:
            return 0
        return 1+self.dfs(root.left)+self.dfs(root.right)
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        return self.search(root,k)
    def search(self,root,k):
        """
        查找以root为根节点找出第K小的数
        :param root:
        :return:
        """
        if not root:
            return
        num_nodes = self.dfs(root.left)
        if num_nodes == k-1:
            return root
        elif num_nodes >= k:
            return self.search(root.left,k)
        elif num_nodes < k:
            return self.search(root.right,k-num_nodes-1)

s = Solution()
print(s.KthNode(root,8))
