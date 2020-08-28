from binarytree import Node
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.left.left.left = Node(8)
print(root1)
string = '1!2!3!4!5!6!7!8!#!#!#!#!#!#!#!#!#!'

class Solution():
    def Serialize(self, root):
        #层次遍历序列化二叉树,注意此时与按行打印二叉树时queue的不同的用法，此时None也要被写入序列化。
        queue,ch = [root],[]
        while queue:
            cur = queue.pop(0)
            if not cur:
                ch.append('#!')
            else:
                queue.append(cur.left) #此时不需要判断左右节点是否为None,if cur.left|if cur.right
                queue.append(cur.right)
                ch.append(str(cur.value)+'!')
        return ''.join(ch)
    def Deserialize(self,s):
        #层次遍历反序列化二叉树
        node_value = s.split('!')[:-1]
        root = Node(int(node_value.pop(0)))
        queue = [root] #还是要用队列来记录插入的位置。
        while queue:
            if not s:
                return None
            l_val = node_value.pop(0)
            r_val = node_value.pop(0)
            q_top = queue.pop(0)
            if l_val != '#' and r_val != '#':
                q_top.left = Node(int(l_val))
                q_top.right = Node(int(r_val))
                queue.append(q_top.left)
                queue.append(q_top.right)
            elif l_val != '#' and r_val == '#':
                q_top.left = Node(int(l_val))
                queue.append(q_top.left)
            elif l_val == '#' and r_val != '#':
                q_top.right = Node(int(r_val))
                queue.append(q_top.right)
        return root

s = Solution()
print(s.Serialize(root1))
# print(s.Deserialize(string))