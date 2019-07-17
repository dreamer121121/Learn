#列表或者元组方式实现二叉树
# def BinTree(data,left=None,right=None):
#     return [data,left,right]
#
# def is_empty_BinTree(btree):
#     return btree is None
#
# def root(btree):
#     return btree[0]
#
# def left(btree):
#     return btree[1]
#
# def right(btree):
#     return btree[2]
#
# def set_root(btree,data):
#     btree[0] = data
#
# def set_left(btree,left):
#     btree[1] = left
#
# def set_right(btree,right):
#     btree[2] = right
#
# #构建一棵二叉树
# t1 = BinTree(2,BinTree(5),BinTree(4))
# set_left(left(t1),BinTree(5))


#定义二叉树类
# class BinTNode:
#     def __init__(self,val,left = None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# root = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(5)),BinTNode(3,BinTNode(6),BinTNode(7)))
#
#
# #二叉树的递归遍历
# def pre(root):
#     """
#     前序遍历二叉树
#     :param root:
#     :return:
#     """
#     if root == None:
#         return
#     print("Node："+str(root.val))
#     pre(root.left)
#     pre(root.right)
#
# def pos(root):
#     """
#     二叉树的后序遍历
#     :param root:
#     :return:
#     """
#     if root is None:
#         return False
#     pos(root.left)
#     pos(root.right)
#     print(root.val)
#
# def mid(root):
#     """
#     二叉树的中序遍历
#     :param root:
#     :return:
#     """
#     if root is None:
#         return False
#     mid(root.left)
#     print(root.val)
#     mid(root.right)
#
# def row_order(tree):
#     # print(tree._data)
#     """
#     二叉树的层次遍历
#     :param tree:
#     :return:
#     """
#     queue = []
#     queue.append(tree)
#     while True:
#         if queue==[]:
#             break
#         print(queue[0]._data)
#         first_tree = queue[0]
#         if first_tree._left != None:
#             queue.append(first_tree._left)
#         if first_tree._right != None:
#             queue.append(first_tree._right)
#         queue.remove(first_tree)
#
# def count_BinTNodes(root):
#     """
#     计算二叉树中的节点个数
#     :param root:
#     :return:
#     """
#     if root == None:
#         return 0
#     else:
#          return 1+count_BinTNodes(root.left)+count_BinTNodes(root.right)
#
# def sum_BinTNodes(root):
#     """
#     计算二叉树中节点和
#     :param root:
#     :return:
#     """
#     if root is None:
#         return 0
#     else:
#         return root.val + sum_BinTNodes(root.left)+sum_BinTNodes(root.right)
#
# pos(root)

#构建BST
# class Node(object):
#
#     def __init__(self,data=None):
#         self._left = None#左节点
#         self._right = None#右节点
#         self._data = data
#
#     def set_left(self,node):
#         self._left = node
#
#     def set_right(self,node):
#         self._right = node
#
#     def get_left(self):
#         return self._left
#
#     def get_right(self):
#         return self._right
#
#     def set_data(self,data):
#         self._data = data
#
#     def get_data(self):
#         return self._data
#
#
# class BSTNode(Node):
#
#     def __init__(self, data=None):
#         Node.__init__(self, data=data)  # 这继承不像c++,不会默认调用父类的构造函数，需要像这样写#或者可以使用super()
#         self.__in_order = []  # 中序遍历的列表
#         self.__pre_order = []  # 前序遍历的列表
#         self.__post_order = []  # 后序遍历的列表
#
#     def insert(self, data):
#         if data < self._data:  # 比此数据小就插左边，否则就插右边
#             if self._left:
#                 return self._left.insert(data)
#             else:
#                 self._left = BSTNode(data)
#         else:
#             if self._right:
#                 return self._right.insert(data)
#             else:
#                 self._right = BSTNode(data)
#
#     @staticmethod  # 静态方法
#     def min_val_bst_node(bst_node):
#         current = bst_node
#         while current._left is not None:
#             current = current._left
#         return current
#
#     def delete(self, data):
#         if self is None:  # 发现没有这个数据时做以下处理
#             return None
#         if data < self._data:  # 要删的数据比此数据小，就从左子树删起
#             self._left = self._left.delete(data)
#         elif data > self.get_data():  # 要删的数据比此数据大，从右子树删起
#             self._right = self._right.delete(data)
#         else:  # 要删的就是此数据
#             if self._left is None:  # 当左子树为空时，返回右子树，那么这个数据就删掉了，返回上层的时候，它的父节点与右子树相连
#                 temp = self._right
#                 return temp
#             elif self._right is None:  # 当右子树为空，与上面相似
#                 temp = self._left
#                 return temp
#         # 如果左右子树都不为空时，把右子树的最左节点（最小结点）和此结点的数据替换
#         temp = self.min_val_bst_node(self._right)
#         self._data = temp._data
#         self._right = self._right.delete(temp._data)
#         return self
#
#     def find(self, data):
#         if data == self.get_data():
#             return True
#         elif data < self.get_data():  # 小就往左子树找，大就往右子树找
#             if self._left:
#                 return self._left.find(data)
#             else:
#                 return False
#         else:
#             if self.get_right():
#                 return self._right.find(data)
#             else:
#                 return False
#
#     # 下面这些函数与纯二叉树的类似
#     def inorder(self, root):
#         if root:
#             self.inorder(root._left)
#             self.__in_order.append(root._data)
#             self.inorder(root._right)
#         return self.__in_order
#
#     def preorder(self, root):
#         if root:
#             self.__pre_order.append(root._data)
#             self.preorder(root._left)
#             self.preorder(root._right)
#         return self.__pre_order
#
#     def postorder(self, root):
#         if root:
#             self.postorder(root._left)
#             self.postorder(root._right)
#             self.__post_order.append(root._data)
#         return self.__post_order
#
#
# class BST(object):
#
#     def __init__(self):
#         self.__root = None
#
#     def insert(self, data):
#         if self.__root:
#             self.__root.insert(data)
#         else:
#             self.__root = BSTNode(data)
#
#     def delete(self, data):
#         if self.__root:
#             return self.__root.delete(data)
#
#     def find(self, data):
#         if self.__root:
#             return self.__root.find(data)
#         else:
#             return False
#
#     def preorder(self):
#         if self.__root:
#             return self.__root.preorder(self.__root)
#
#     def inorder(self):
#         if self.__root:
#             return self.__root.inorder(self.__root)
#
#     def postorder(self):
#         if self.__root:
#             return self.__root.postorder(self.__root)
#
#     def __numbers_of_nodes_help(self, root):
#         if root:
#             return self.__numbers_of_nodes_help(root._left) + self.__numbers_of_nodes_help(root._right) + 1
#         else:
#             return 0
#
#     def numbers_of_nodes(self):
#         return self.__numbers_of_nodes_help(self.__root)
#
#
# mylist = [8,5,10,2,6,9,11]
# bst = BST()
# for data in mylist:
#     bst.insert(data)
#
# print(bst.numbers_of_nodes())


class Node():
    def __init__(self,data = None):
        self._left = None
        self._right = None
        self._data = data


#
class BinaryTree():

    def __init__(self):
        self._root = None
        self._length = 0
    # def insert(self,item):

    #     """
    #     利用迭代的方式创建二叉树
    #     item,需要插入的数据
    #     queue用来找到该插入的位置
    #     :param item:
    #     :return:
    #     """
    #     node = Node(item)
    #     if self._root is None:
    #         """如果根结点是None,是一颗空数,我们就把node赋值给root,那么下面的while循环是不会受影响的,因为是队列[None]的bool值是True"""
    #         self._root = node
    #         self._length += 1
    #         return
    #
    #     queue = [self._root] #维护一个队列用于查找该插入的位置
    #
    #     while queue:
    #         """队列的弹出要加0,与栈相仿"""
    #         cur_node = queue.pop(0)
    #         if cur_node._left is None:
    #             """这里有空位,我们插入结点,如果能插入,就完事了"""
    #             cur_node._left = node
    #             self._length += 1
    #             return
    #         else:
    #             """cur_node的左孩子我们放进队列中,下次循环左子结点"""
    #             queue.append(cur_node._left)
    #
    #         """同理对右边的操作一样,还是手敲下吧"""
    #
    #         if cur_node._right is None:
    #             cur_node._right = node
    #             self._length += 1
    #             return
    #         else:
    #             queue.append(cur_node._right)


    def listcreattree(root, llist, i):  ###用列表递归创建二叉树，
        # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
        # 再接着创建b的右子树，
        if i < len(llist):
            if llist[i] == '#':
                return None  ###这里的return很重要
            else:
                root = Node(llist[i])
                print('列表序号：' + str(i) + ' 二叉树的值：' + str(root._data))
                # 往左递推
                root.left = self.listcreattree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
                # 往右回溯
                root.right = self.listcreattree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
                # 再返回根'
                print('************返回根：', root._data)
                return root  ###这里的return很重要
        return root

    def preorder(self,root):
        if root == None:
            return
        print(root._data)
        self.preorder(root._left)
        self.preorder(root._right)

    def midorder(self,root):
        if root == None:
            return False
        self.midorder(root._left)
        print(root._data)
        self.midorder(root._right)

    def postorder(self,root):

        if root == None:
            return False
        self.postorder(root._left)
        self.postorder(root._right)
        print(root._data)

    def level(self,root):
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur._data)
            if cur._left != None:
                queue.append(cur._left)
            if cur._right != None:
                queue.append(cur._right)

#
# ele = [1,2,3,4,5,6,7]
# tree = BinaryTree()
#
# while ele:
#     tree.insert(tree._root,ele.pop(0)) #一次直插入一个元素
#
# print("--tree.length--",tree._length)
# print("preorder：\n")
# tree.preorder(tree._root)
# print("midorder:\n")
# tree.midorder(tree._root)
# print("postorder:\n")
# tree.postorder(tree._root)
# print("level:\n")
# tree.level(tree._root)


from binarytree import tree
mytree = tree()
print(mytree)






