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
class BinTNode:
    def __init__(self,val,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

root = BinTNode(1,BinTNode(2,BinTNode(4),BinTNode(5)),BinTNode(3,BinTNode(6),BinTNode(7)))


#二叉树的递归遍历
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

def pos(root):
    """
    二叉树的后序遍历
    :param root:
    :return:
    """
    if root is None:
        return False
    pos(root.left)
    pos(root.right)
    print(root.val)

def mid(root):
    """
    二叉树的中序遍历
    :param root:
    :return:
    """
    if root is None:
        return False
    mid(root.left)
    print(root.val)
    mid(root.right)

def row_order(tree):
    # print(tree._data)
    """
    二叉树的层次遍历
    :param tree:
    :return:
    """
    queue = []
    queue.append(tree)
    while True:
        if queue==[]:
            break
        print(queue[0]._data)
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.append(first_tree._right)
        queue.remove(first_tree)

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

pos(root)



