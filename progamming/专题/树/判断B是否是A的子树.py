from binarytree import Node
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.left.left.left = Node(8)
root2 = Node(4)
root2.left = Node(8)
root3 = Node(10)
root3.left = Node(11)

#问题在于如何通过读题分析出来是一个递归问题。
class Solution():
    def HasSubtree(self, pRoot1, pRoot2):

        if not pRoot1 or not pRoot2: #递归终止条件
            return False

        return self.is_subtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def is_subtree(self,root1,root2):
        #这两个递归终止条件十分重要。
        if not root2:
            return True
        if not root1 or root1.value != root2.value: #递归终止条件
            return False
        return self.is_subtree(root1.left,root2.left) and self.is_subtree(root1.right,root2.right)



s = Solution()
print(s.HasSubtree(root1,root3))