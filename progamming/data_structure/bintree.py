def BinTree(data,left=None,right=None):
    return [data,left,right]

def is_empty_BinTree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree,data):
    btree[0] = data

def set_left(btree,left):
    btree[1] = left

def set_right(btree,right):
    btree[2] = right

#构建一棵二叉树
t1 = BinTree(2,BinTree(5),BinTree(4))
set_left(left(t1),BinTree(5))


