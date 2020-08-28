from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
root.right.right.right.right = Node(9)
print(root)
#核心思想：判断一棵树是否是AVL,判断左右子树的深度绝对值之差是否小于等于1
def IsBalanced_Solution(root):#定义函数：判断是否是是一颗平衡二叉树
    if not root:
        return True
    if abs(TreeDepth(root.left)-TreeDepth(root.right)) > 1:
        return False
    return IsBalanced_Solution(root.left) and IsBalanced_Solution(root.right)

def TreeDepth(root): #定义函数：返回以当前节点为根节点的树的深度
    if not root:
        return 0
    return max(TreeDepth(root.left),TreeDepth(root.right))+1
print(IsBalanced_Solution(root))