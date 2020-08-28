from binarytree import tree,Node
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.left.left = Node(15)
root.left.right = Node(17)
print(root)
class Solution():
    def __init__(self):
        self.result = []
    def Print_row(self,root):
        if not root:
            return None
        r_index = 1
        queue = [root]
        last = root
        tmp = []
        while queue:
            top = queue[0]
            tmp.append(top.value)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
            nlast = queue[-1]
            if queue.pop(0) == last:
                self.result.append(tmp)
                tmp = []
                last = nlast
s = Solution()
s.Print_row(root)
print(s.result)

