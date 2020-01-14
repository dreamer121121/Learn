from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.left = Node(9)
print(root)

class Solution():
    def IsBalanced_Solution(self, pRoot):
        if not pRoot: #空树是平衡二叉树
            return True

        #左右两颗子树的深度差是否超过1,超过1则不是平衡二叉树
        l_depth = self.Treedepth(root.left)
        r_depth = self.Treedepth(root.right)
        if abs(l_depth-r_depth) > 1:
            return False

        #判断左右子树是否是平衡二叉树
        is_left = self.IsBalanced_Solution(pRoot.left)
        is_right = self.IsBalanced_Solution(pRoot.right)

        return is_right and is_left

    def Treedepth(self,root):
        #计算树的高度
        if not root:
            return 0
        l_depth = self.Treedepth(root.left)
        r_depth = self.Treedepth(root.right)
        return max(l_depth,r_depth)+1


s = Solution()
print(s.IsBalanced_Solution(root))