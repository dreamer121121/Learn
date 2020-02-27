from binarytree import Node
class Solution():
    def reconstructBinaryTree(self,pre,tin):
        #已知前序遍历和中序遍历重建二叉树
        if len(pre) > 0:
            root_index = tin.index(pre[0]) #在中序遍历中找到前序遍历的第一个数字所在的位置
            root = Node(pre[0])
            if self._root is None:
                self._root = root
            root.left = self.reconstructBinaryTree(pre[1:root_index+1],tin[:root_index])    #reconstructBinaryTree必须要有返回值
            root.right = self.reconstructBinaryTree(pre[root_index+1:],tin[root_index+1:])
            return root
        else:
            return None

s = Solution()
print(s.reconstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]))

