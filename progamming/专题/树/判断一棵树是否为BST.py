class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        max_l = self.search(root.left, label='l')
        min_r = self.search(root.right, label='r')
        if max_l >= root.val or min_r <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def search(self, root, label):
        if not root and label == 'l':
            return -float('inf')
        if not root and label == 'r':
            return float('inf')
        result = []
        queue = [root]
        while queue:
            top = queue.pop(0)
            result.append(top.val)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        if label == 'l':
            return max(result)
        elif label == 'r':
            return min(result)







