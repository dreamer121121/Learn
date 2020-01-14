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
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result = []
    def FindPath(self,root,target):
        if not root:
            return []
        path = []
        self.Find(root,target,path)
    def Find(self,root,target,path):
        if not root:
            return
        path.append(root.value)
        if not root.left and not root.right and sum(path) == target:
            #是叶节点
            self.result.append(path[:]) #进行深拷贝，此处若直接self.result.append(path)会出错
        self.Find(root.left,target,path)
        self.Find(root.right,target,path)
        path.pop() #回退，要理解为何要弹出

s = Solution()
s.FindPath(root,10)
print(s.result)
