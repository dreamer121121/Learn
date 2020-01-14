from binarytree import tree,Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(root)
class Solution():
    def __init__(self):
        self.result = []
    def Print(self, pRoot):
        queue = [pRoot] #建立一个队列
        while queue:
            tmp = []
            row_size = len(queue)
            for i in range(row_size):
                cur = queue.pop(0)
                tmp.append(cur.value)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            self.result.append(tmp)
        print('s.result:',s.result)

s = Solution()
s.Print(root)
for depth in range(len(s.result)):
    if (depth + 1) % 2 == 0:
        for num in s.result[depth][::-1]:
            print(num)
    else:
        for num in s.result[depth]:
            print(num)
    print('-------------------------')
