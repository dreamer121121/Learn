
class Node(object):
    def __init__(self,element):
        self.element=element
        self.lchild=None
        self.rchild=None

class Tree(object):
    def __init__(self):
        self.root=None
        self.length = 0

    def mid(self,root):
        """
        二叉树的中序遍历
        :param root:
        :return:
        """
        if root is None:
            return False
        self.mid(root.lchild)
        print(root.element)
        self.mid(root.rchild)

    def add(self,cur,item):
        if self.root == None:
            self.root = Node(item)
            self.length += 1
            return
        if item < cur.element:
            if cur.lchild:
                self.add(cur.lchild,item)
            else:
                cur.lchild = Node(item)
                self.length += 1
        elif item > cur.element:
            if cur.rchild:
                self.add(cur.rchild,item)
            else:
                cur.rchild = Node(item)
                self.length += 1

    def level(self,root):
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.element)
            if cur.lchild != None:
                queue.append(cur.lchild)
            if cur.rchild!= None:
                queue.append(cur.rchild)

data = [17,5,35,2,11,29,38,9,16,8]
tree = Tree()
while data:
    cur_data = data.pop(0)
    tree.add(tree.root,cur_data)

print("length:"+str(tree.length))
print("levelorder:")
tree.level(tree.root)
# print("midorder:")
# tree.mid(tree.root)


