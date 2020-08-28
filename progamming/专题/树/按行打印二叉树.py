from binarytree import Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)


def levelOrderBottom(root):
    if not root:
        return []
    queue = [root]
    last = queue[0]
    nlast = queue[0]
    result = []
    path = []
    while queue:
        top = queue[0] #查看队顶元素。
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)
        nlast = queue[-1]
        top = queue.pop(0)
        path.append(top.value)
        if top == last:
            result.append(path[:])
            path = []
            last = nlast
    return result

print(levelOrderBottom(root))
