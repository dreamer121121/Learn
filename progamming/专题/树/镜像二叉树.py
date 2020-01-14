from binarytree import Node
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.left.left.left = Node(8)
print(root1)
class Solution():
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:#递归终止条件
            return
        root.left,root.right = root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)

s = Solution()
s.Mirror(root1)
print(root1)
