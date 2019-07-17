



class Node(object):
    def __init__(self,element):
        self.element=element
        self.lchild=None
        self.rchild=None



class Tree(object):

    def __init__(self,root=None):
        self.root=root
        self.length = 0

    def add(self,cur,item):
        if cur is None:
            cur=Node(item)
            self.length += 1
            return
        else:
            """递归的寻找该在哪插入数据"""
            if(item<cur.element):
                cur=cur.lchild
                self.add(cur,item)
            elif(item>cur.element):
                cur=cur.rchild
                self.add(cur,item)


    def level(self,root):
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.element)
            if cur.lchild != None:
                queue.append(cur.lchild)
            if cur.rchild!= None:
                queue.append(cur.rchild)



data = [1,2,3,4,5,56,12,48]
tree = Tree()
while data:
    cur_data = data.pop(0)
    tree.add(tree.root,cur_data)
print(tree.root)
#
# print("length:"+str(tree.length))
# print("levelorder:")
# tree.level(tree.root)

