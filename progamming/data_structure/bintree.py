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

class BinTNode:
    def __init__(self,val,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

root = BinTNode(1,BinTNode(2),BinTNode(3))


def pre(root):
    """
    前序遍历二叉树
    :param root:
    :return:
    """
    if root == None:
        return
    print("Node："+str(root.val))
    pre(root.left)
    pre(root.right)

def count_BinTNodes(root):
    """
    计算二叉树中的节点个数
    :param root:
    :return:
    """
    if root == None:
        return 0
    else:
         return 1+count_BinTNodes(root.left)+count_BinTNodes(root.right)

def sum_BinTNodes(root):
    """
    计算二叉树中节点和
    :param root:
    :return:
    """
    if root is None:
        return 0
    else:
        return root.val + sum_BinTNodes(root.left)+sum_BinTNodes(root.right)

