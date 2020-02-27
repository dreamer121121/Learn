from binarytree import Node
root1 = Node(8)
root1.left = Node(8)
root1.right = Node(7)
root1.left.left = Node(9)
root1.left.right = Node(2)
root1.left.right.left = Node(4)
root1.left.right.right = Node(7)
root2 = Node(8)
root2.left = Node(9)
root2.right = Node(2)
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

class Solution2():
    def HasSubtree(self, pRoot1, pRoot2):

        if not pRoot1 or not pRoot2: #递归终止条件
            return False

        return self.is_subtree(pRoot1,pRoot2)

    def is_subtree(self,root1,root2):
        #这两个递归终止条件十分重要。
        if not root2:
            return True
        if not root1: #递归终止条件
            return False
        if root1.value == root2.value:
            return self.is_subtree(root1.left,root2.left) and self.is_subtree(root1.right,root2.right)
        else:#园艺是想重新开一个新头，但是在递归中是不能实现的。
            return self.is_subtree(root1.left,root2) or self.is_subtree(root1.right,root2)

print("root1")
print(root1)
print('root2')
print(root2)
s = Solution2()
print(s.HasSubtree(root1,root2))