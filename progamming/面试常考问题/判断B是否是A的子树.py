from binarytree import Node
root1 = Node(8)
root1.left = Node(8)
root1.right = Node(7)
root1.left.left = Node(9)
root1.left.right = Node(2)
root1.left.right.left = Node(4)
root1.left.right.right = Node(7)
root2 = Node(8)
root2.left = Node(9)
root2.right = Node(2)
# root3 = Node(10)
# root3.left = Node(11)
def judgesubtree(root1,root2):
    if not root1 or not root2:
        return  False
    return judgeeuql(root1,root2) or judgesubtree(root1.left,root2) or judgesubtree(root1.right,root2)

def judgeeuql(root1,root2):
    """判1断两棵树是否相同"""
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    else:
        return judgeeuql(root1.left,root2.left) and judgeeuql(root1.right,root2.right)

