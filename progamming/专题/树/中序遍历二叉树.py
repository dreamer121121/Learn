from binarytree import tree
root = tree()
print(root)
#递归法进行中序遍历
def mid(root):
    if root is None:
        return
    mid(root.left)
    print(root.value)
    mid(root.right)
mid(root)
#迭代法中序遍历二叉树
def mid_itera(root):
    stack = []
    result = []
    node = root
    while node or len(stack) > 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.value) #保证先遍历自己再遍历右边。
            node = node.right
    return result
print(mid_itera(root))

