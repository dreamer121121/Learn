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
            cur = Node(l,eletoTree,parent)

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
            print(cur.l)
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
            print("l:",l)
            if abs(t[l]-cur.value[l])<self.nearestvalue and cur != leaf: #因为是从当前点开始往回搜索，最开始的叶子结点的abs(t[l]-cu.value[l])必然小与self.nerastvalue
                print("t[l]>cur.value[l]")
                #这两句判断句对应算法中的：在当前子节点的父节点的另一个子节点所对应的区域中进行搜索
                if t[l] <= cur.value[l] and cur.rchild:
                    travel(cur.rchild,t)
                elif t[l] > cur.value[l] and cur.lchild:
                    travel(cur.lchild,t)
                #这两句判断句对应算法中的：在当前子节点的父节点的另一个子节点所对应的区域中进行搜索
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
        print("leaf:",leaf.value)
        #递归向上搜索
        result = self.fdNN(leaf,ele)

        return result


    def maintain_heap(self,i):
        """
        从堆顶开始调整
        :param i:
        :return:
        """
        left = 2*i+1
        right = 2*i+2
        if left < self.heap_length and self.heap[left][1] > self.heap[i][1]:
            largest = left
        elif right < self.heap_length and self.heap[right][1] > self.heap[i][1]:
            largest = right
        else:
            largest = i
        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.maintain_heap(largest)


    def searchKNN(self,ele,k):
        """
        此方法返回与输入值最接近的K个节点
        :param ele:
        :return:
        """
        self.heap = [] #创建一个空堆
        self.heap_length = 0
        self.k = k
        def search(cur,t):
            self.maintain_heap(0)
            print("self.heap:",self.heap)
            print("selg.heap_length",self.heap_length)
            if cur is None: #递归边界：到达叶节点
                return
            l = cur.l
            cur2t_dis = self.compute_dis(cur.value,t)
            print("cur.value:",cur.value)
            print("cur2t_dis",cur2t_dis)
            if self.heap:
                heaptop = self.heap[0]
                heaptop_dis = heaptop[1]
                if self.heap_length < self.k:
                    self.heap.append([cur,self.compute_dis(cur.value,t)])
                    self.heap_length += 1
                    self.maintain_heap(0)

                elif  cur2t_dis < heaptop_dis:
                    self.heap[0] = [cur,self.compute_dis(cur.value,t)]
                    self.maintain_heap(0)

                if self.heap_length < self.k or abs(cur.value[l]-t[l]) < heaptop_dis:
                    search(cur.lchild,t)
                    search(cur.rchild,t)
                elif t[l] < cur.value[l]:
                    search(cur.lchild,t)
                else:
                    search(cur.rchild,t)
            else:
                self.heap.append([cur, self.compute_dis(cur.value, t)])
                self.heap_length += 1
                search(cur.lchild,ele)
                search(cur.rchild,ele)
        search(self.root,ele)

        return sorted(self.heap,key=lambda x:x[1])



#--------------------------------------------------------------------------------------------

def compute_dis(ele,t):
    return np.linalg.norm(np.array(ele)-np.array(t))



def test(elements,t):
    trace = []
    min_diss = float("inf")
    match_node = (float("inf"),float("inf"))
    for ele in elements:
        diss = compute_dis(ele,t)
        trace.append((ele,diss))
        if diss < min_diss:
            min_diss = diss
            match_node = ele
    trace.sort(key=lambda x:x[1])
    return match_node,min_diss,trace



if __name__ == "__main__":
    elements = [[7,2],[5,4],[9,6],[2,3],[3,5],[8,1]]
    kd = KD_tree()
    kd.create_tree(kd.root,0,elements,2)

    # print("search result:",kd.searchNN((3,4.5)).value)
    # kd.levelorder()

    # kd.searchNN((6,8))
    #验证
    # print("--验证：--",test(elements,[3,4.5]))
    k = 2
    result = kd.searchKNN((3,4.5),2)
    print("-----KD-KNN-----")
    for i in range(k):
        print(result[i][0].value,result[i][1])
    #验证
    print("--验证：--",test(elements,[3,4.5])[2][:2])





