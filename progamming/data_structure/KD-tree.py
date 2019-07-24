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

    def create_tree(self,cur,elements_list):

        if not elements_list:#递归边界
            return
        elements_array = np.array(elements_list,dtype=int)
        print("elements_array",elements_array)
        #选特征
        var_list = np.var(elements_array, 0)
        feature_index = np.argmax(var_list)  # 返回方差最大特征的索引
        print("feature_index:",feature_index)
        # 找到当前需要入树的元素
        num_ele = len(elements_array[:,feature_index].tolist())
        mid = num_ele // 2
        elements_array = np.sort(elements_array,axis=0)
        print("sorted_elements_array",elements_array)
        eletoTree = elements_array[mid,:]
        print("eletoTree",eletoTree)
        #根据当前节点对数据集进行划分
        leftarray = elements_array[:mid,:]
        rightarray = elements_array[mid+1:,:]
        print("leftarray:",leftarray)
        print("rightarray:",rightarray)
        # if num_ele%2 == 0:
        #     elements_array = np.sort(elements_array,axis= 0)
        #     mid = num_ele // 2
        #     eletoTree = elements_array[mid,:]
        #
        # else:
        #     ele_index =elements_array[:,feature_index].tolist().index(int(np.median(elements_array[:,feature_index])))
        #     eletoTree = elements_array[ele_index,:]
        #用当前节点对数据做划分

        #该往哪里插？
        if self.root is None:
            self.root = Node(eletoTree)
        #
        # if cur is None:
        #     cur = Node(eletoTree)





kd = KD_tree()
kd.create_tree(kd.root,[[7,2],[5,4],[9,6],[2,3],[4,7],[8,1]])
print(kd.root)





