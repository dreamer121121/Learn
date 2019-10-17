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


    def KthNode(self,root,k):
        self.result = []
        def mid(root):
            """中序遍历BST能得到有序的列表"""
            if root == None:
                return
            mid(root.left)
            self.result.append(root.value)
            mid(root.right)
        mid(root)
        return self.result[k-1]

    def KthNode2(self,root,k):
        """采用分治法仔细体会。"""
        def count(node):
            if not node:
                return 0
            return 1+count(node.left)+count(node.right)
        count = count(root.left)#统计左子树的节点的个数
        if k <= count:
            return self.KthNode2(root.left,k)
        elif k>count+1:
            return self.KthNode2(root.right,k-count-1)
        return root.value #k==count+1时返回

data = [17,5,35,2,11,29,38,9,16,8]
tree = Tree()
while data:
    cur_data = data.pop(0)
    tree.add(tree.root,cur_data)
print(tree.root)
print(tree.KthNode2(tree.root,3))

