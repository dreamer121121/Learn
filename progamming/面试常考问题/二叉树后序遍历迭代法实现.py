from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)

#使用迭代法实现二叉树的前序和后序遍历

# def post(root):
#     """
#     层次遍历时使用的queue
#     :param root:
#     :return:
#     """
#     l = []
#     stack = []
#     if root == None: return []
#     stack.append(root)
#     while stack != []:
#         N = stack.pop()
#         l.append(N.value)
#         if N.left != None: stack.append(N.left)
#         if N.right != None: stack.append(N.right)
#     return l[::-1]
# print(post(root))




def first(root):
    res = []
    stack = [root]
    while stack:
        top = stack.pop()
        res.append(top.value)
        if  top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)
    return res
print(first(root))