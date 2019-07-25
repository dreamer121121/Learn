import numpy as np

class Node:
    def __init__(self,ele):
        self.xvalue = ele[0]
        self.yvalue = ele[1]
        self.lchild = None
        self.rchild = None

class KD_tree:
    def __init__(self):
        self.root = None

    def create_tree(self,cur,depth,elements_list,k):
        if not elements_list:#递归边界
            return
        #确定使用第几个特征进行数据集划分
        if self.root is None:#此处单独把根节点拿出来做特殊处理
            l = 0
        else:
            l = depth % k

        # 找到当前需要入树的元素
        num_ele = len(elements_list)
        elements_list.sort(key=lambda x:x[l]) #按指定的特征对数据集进行排序
        mid = num_ele // 2
        eletoTree = elements_list[mid]
        elements_array = np.array(elements_list,dtype=int)

        #根据当前节点对数据集进行划分
        left_list = elements_array[:mid,:].tolist()
        right_list = elements_array[mid+1:,:].tolist()

        #每一次递归中如何找到插入数据的位置
        if self.root is None:#此处单独处理树的根节点
            self.root = Node(eletoTree)
            cur = self.root

        if cur is None:
            cur = Node(eletoTree)

        cur.lchild = self.create_tree(cur.lchild,depth+1,left_list,k)
        cur.rchild = self.create_tree(cur.rchild,depth+1,right_list,k)

        return cur

    def levelorder(self):
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.xvalue)
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)

kd = KD_tree()
kd.create_tree(kd.root,0,[[7,2],[5,4],[9,6],[2,3],[4,7],[8,1]],2)
print(kd.levelorder())




