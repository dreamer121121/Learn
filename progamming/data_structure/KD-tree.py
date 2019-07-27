import numpy as np



class Node:
    def __init__(self,l,ele,parent=None):
        self.value = tuple(ele)
        self.parent = parent
        self.lchild = None
        self.rchild = None
        self.l = l

class KD_tree:

    def __init__(self):
        self.root = None

    def create_tree(self,cur,depth,elements_list,k,parent=None):

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
            self.root = Node(l,eletoTree,parent)#根节点的父节点为None
            cur = self.root

        if cur is None:
            cur = Node(1,eletoTree,parent)

        cur.lchild = self.create_tree(cur.lchild,depth+1,left_list,k,cur)
        cur.rchild = self.create_tree(cur.rchild,depth+1,right_list,k,cur)
        return cur

    def levelorder(self):
        """
        此方法用于KD树的层次遍历
        :return:
        """
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.value)
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)

    def fdleaf(self,cur,ele):
        target = Node(-1,(float('inf'),float('inf')))
        l = cur.l
        if ele[l] < cur.value[l]:
            if cur.lchild:
                target = self.fdleaf(cur.lchild,ele)
            else:
                target = cur
        elif ele[l] >= cur.value[l]:
            if cur.rchild:
                target = self.fdleaf(cur.rchild,ele)
            else:
                target = cur
        return target


    def compute_dis(self,a,b):
        return np.linalg.norm(np.array(a)-np.array(b))


    def fdNN(self,leaf,t):
        self.nearestpoint = None
        self.nearestvalue = 0
        leaf_dis = self.compute_dis(t,leaf.value)
        def travel(cur,t):
            """
            由叶节点向根节点回溯
            :param cur:
            :param t:
            :return:
            """
            print("current nearstvalue:",self.nearestvalue)
            if cur is None: #说明到根节点了
                return
            mindis = self.compute_dis(cur.value,t)
            if self.nearestpoint is None:
                self.nearestpoint = cur
                self.nearestvalue = mindis
            elif self.nearestvalue > mindis:
                self.nearestpoint = cur
                self.nearestvalue = mindis

            l = cur.l
            if abs(t[l]-cur.value[l])<self.nearestvalue and self.compute_dis(t,cur.value) != leaf_dis: #因为是从当前点开始往回搜索，最开始的叶子结点的abs(t[l]-cu.value[l])必然小与self.nerastvalue
                if t[l] <= cur.value[l] and cur.rchild:
                    travel(cur.rchild,t)
                elif t[l] > cur.value[l] and cur.lchild:
                    travel(cur.lchild,t)
            else:
                travel(cur.parent,t)

        travel(leaf,t)
        return self.nearestpoint

    def searchNN(self,ele):
        """
        此方法用于寻找在KD树中寻找最近邻的元素
        :param ele:
        :return:
        """
        #1找到包含目标点的叶子节点
        leaf = self.fdleaf(self.root,ele)
        print("--leaf.value--:",leaf.value)
        #递归向上搜索
        result = self.fdNN(leaf,ele)

        return result



def compute_dis(ele,t):
    return np.linalg.norm(np.array(ele)-np.array(t))



def test(elements,t):
    min_diss = float("inf")
    match_node = (float("inf"),float("inf"))
    for ele in elements:
        diss = compute_dis(ele,t)
        if diss < min_diss:
            min_diss = diss
            match_node = ele
    return match_node



if __name__ == "__main__":
    elements = [[7,2],[5,4],[9,6],[2,3],[4,7],[8,1]]
    kd = KD_tree()
    kd.create_tree(kd.root,0,elements,2)
    print("search result:",kd.searchNN((5,4)).value)

    # kd.levelorder()

    # kd.searchNN((6,8))
    #验证
    # print("--验证：--",test(elements,(5,4)))
    #





