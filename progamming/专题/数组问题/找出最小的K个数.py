class Solution:
    # def GetLeastNumbers_Solution(self, tinput, k):
    #     #方法一：排序-->tinput[:k] 时间复杂度：O(nlogn)
    #     if not tinput or  k <= 0:
    #         return []
    #     if len(tinput) < k:
    #         return None
    #     tinput.sort()
    #     return tinput[:k]
        #维护一个大顶堆,若当前的值小于堆顶值则将当前值与堆顶值替换，维护大顶堆
    def GetLeastNumbers_Solution(self,tinput,k):
        init_ele = tinput[:] #深拷贝
        heap_eles = init_ele[:k]
        heap = self.init_heap(heap_eles)
        for i in range(k,len(tinput)):
            if tinput[i] < heap[0]:
                heap[0] = tinput[i]
                self.maintain_heap(heap,0)
        return heap
    def init_heap(self,eles):
        mid = len(eles) // 2 -1
        for i in range(mid,-1,-1):
            self.maintain_heap(eles,i)
        return eles #建好的大顶堆

    def maintain_heap(self,eles,i):
        #从i向下调整。
        heap_size = len(eles)
        left = 2*i+1
        right = 2*i +2
        largest = i
        if left < heap_size and eles[left] > eles[largest]:
            largest = left
        if right < heap_size and eles[right] > eles[largest]:
            largest = right
        if i != largest:
            eles[i],eles[largest] = eles[largest],eles[i]
            self.maintain_heap(eles,largest)
        else:
            return

s = Solution()
print(s.GetLeastNumbers_Solution([4,5,7,0,3,12,23,45,8],3))
