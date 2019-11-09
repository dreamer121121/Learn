from binarytree import Node
class Tree(object):
    def __init__(self):
        self.root=None
        self.length = 0

    def add(self,cur,item):
        """
        递归查找在哪插入元素。
        :param cur:
        :param item:
        :return:
        """
        if self.root == None:
            self.root = Node(item)
            self.length += 1
            return
        if item < cur.value:
            """值小于当前节点的值在左子树上寻找位置"""
            if cur.left:
                self.add(cur.left,item)
            else:
                cur.left = Node(item)
                self.length += 1
        elif item > cur.value:
            """值大于当前节点的值故在其右子树上寻找位置"""
            if cur.right:
                self.add(cur.right,item)
            else:
                cur.right = Node(item)
                self.length += 1

class Solution:
    def Convert(self,pRootTree):
        self.sequence = []
        def mid(root):
            if root == None:
                return
            mid(root.left)
            self.sequence.append(root.value)
            mid(root.right)
        mid(pRootTree)
        for i in range(len(self.sequence)):
            node = self.sequence[i]
            if i>0 and i<len(self.sequence)-1:
                node.left = self.sequence[i-1]
                node.right = self.sequence[i+1]
            elif i==0:
                node.right = self.sequence[i+1]
            elif i==len(self.sequence)-1:
                node.left = self.sequence[i-1]
        return self.sequence

data = [17,5,35,2,11,29,38,9,16,8]
tree = Tree()
while data:
    cur_data = data.pop(0)
    tree.add(tree.root,cur_data)
