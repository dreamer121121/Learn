from binarytree import Node
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

class Solution():
    def isSameTree(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.value != root2.value:
            return False
        return self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)

s = Solution()
print(s.isSameTree(root1,root2))