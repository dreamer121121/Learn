from binarytree import tree,Node
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.left.left = Node(15)
root.left.right = Node(17)
root.right.left = Node(16)
root.right.right = Node(18)
print(root)

class Solution():
    def __init__(self):
        self.result = []
    def Print_row(self,root):
        if not root:
            return None
        r_index = 0
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
                if not r_index % 2:
                    self.result.append(tmp)
                else:
                    self.result.append(tmp[::-1])
                tmp = []
                last = nlast
                r_index += 1
s = Solution()
s.Print_row(root)
print(s.result)