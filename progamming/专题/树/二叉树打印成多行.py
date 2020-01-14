from binarytree import tree,Node
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.left.left = Node(15)
root.left.right = Node(17)
print(root)
queue = [root]
result = []
#关键：同一层的元素同时入队，将某一层的元素出队的同时下一层的元素入队。
while queue:
    # current = queue[0]
    # if current.left:
    #     queue.append(current.left)
    # if current.right:
    #     queue.append(current.right)
    # nlast = queue[-1]
    # print(queue.pop(0).value)
    # if current == last:
    #     print('------------------\n')
    #     last = nlast
    tmp= []
    row_size = len(queue)
    for i in queue:
        tmp.append(i.value)
    result.append(tmp)
    for j in range(len(queue)):
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
print(result)

