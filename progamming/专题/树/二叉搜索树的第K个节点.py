from binarytree import Node
root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(13)
print(root)

class Solution():
    # 返回对应节点TreeNode
    def __init__(self):
        self.nodes = []
    def KthNode(self, pRoot, k):
        self.midorder(pRoot)
        return self.nodes[k-1]
    def midorder(self,root):
        if not root:
            return
        self.midorder(root.left)
        self.nodes.append(root)
        self.midorder(root.right)

s = Solution()
print(s.KthNode(root,3))
