from binarytree import Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)
#给定一颗二叉树，将其转换为一个链表。

def flatten(root):
    """
    迭代法
    :param root:
    :return:
    """
    while root:
        if not root.left:
            root = root.right
        else:
            pre = root.left
            while pre.right:#当前节点左子树最右边节点。
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None
pre = None #记录当前节点的前一节点。
def flatten2(root):
    if not root:
        return
    flatten2(root.right)
    flatten2(root.left)
    global pre
    root.right = pre
    pre = root
flatten(root)