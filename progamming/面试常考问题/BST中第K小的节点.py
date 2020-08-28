#方法一：递归进行中序遍历，用一个数组存储节点，直接取出第K个值
#方法二：采用类似于快排的思想，可以类比于在数组中寻找第K小的数，但是在树中必须要
#定义一个一个函数来计算当前这颗树的节点的个数

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k < 0:
            return None
        cnt = self.count(pRoot.left)
        if cnt >= k:
            return self.KthNode(pRoot.left, k)
        elif cnt+1 < k:
            return self.KthNode(pRoot.right, k-cnt-1)
        else:
            return pRoot
    def count(self,root):
        if not root:
            return 0
        return self.count(root.left)+self.count(root.right)+1