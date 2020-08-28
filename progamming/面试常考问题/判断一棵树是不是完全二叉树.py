from binarytree import Node
root = Node(8)
root.left = Node(8)
root.right = Node(7)
root.left.left = Node(9)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(7)
print(root)

def judge(root):
    if not root:
        return False
    flag = 0
    queue = [root]
    while queue:
        top = queue.pop(0)
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)
        if not top.left and top.right:
            return False
        if flag:#表示已经出现了叶节点
            if top.left or top.right:
                return False
        if (top.left and not top.right) or (not top.left and not top.right):
            flag = 1
    return True

if judge(root):
    print("TRUE")
else:
    print("FALSE")
