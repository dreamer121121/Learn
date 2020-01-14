from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)
class Solution():
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        l_length = self.TreeDepth(pRoot.left)
        r_length = self.TreeDepth(pRoot.right)
        return max(l_length,r_length)+1
s = Solution()
print(s.TreeDepth(root))