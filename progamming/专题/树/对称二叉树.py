from binarytree import Node

class Solution():
    def isSymmetrical(self, pRoot):
        #分别对左右子树进行前序遍历
        if not pRoot:
            return True

        return self.resursiveTree(pRoot.left,pRoot.right)

    def resursiveTree(self,left,right):
        #函数定义：判断两棵树是否是关于中轴线对称的（相信他能实现！）
        #递归终止条件此处三个递归终止条件的顺序要注意一下，互相可以作为筛选条件。
        #判断是否都为None
        if not left and not right:
            return True
        #left and right 有一个为None
        if not left or not right:
            return False
        #经过前两个条件，此处已经能够保证left和right都不是None了。
        if left.value == right.value:
            self.resursiveTree(left.left,right.right) and self.resursiveTree(left.right,right.left)
