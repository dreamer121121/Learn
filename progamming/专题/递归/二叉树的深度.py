from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)

#核心思想：求一颗二叉树的深度=max(左子树的深度,右子树的深度)+1
def TreeDepth(root): #定义函数：返回以当前节点为根节点的树的深度
    if not root:
        return 0
    return max(TreeDepth(root.left),TreeDepth(root.right))+1
print(TreeDepth(root))