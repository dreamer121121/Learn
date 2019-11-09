from binarytree import Node

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return list()

        return self._generateTrees(1, n)

    def _generateTrees(self, left, right):
        if left > right:
            return [None]

        res = list()
        for i in range(left, right + 1):
            left_nodes = self._generateTrees(left, i - 1) #返回的是一个列表，表示以当前点为根节点的所有左BST。
            right_nodes = self._generateTrees(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = Node(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)

        return res
soulution = Solution()
print(soulution.generateTrees(3))