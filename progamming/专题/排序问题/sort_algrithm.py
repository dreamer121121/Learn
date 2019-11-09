a = [1,10,45,23,6,9,2,66]

"""计算逆序对数"""
# class Inverse_nm():
#
#     def __init__(self):
#         self.count = 0
#
#     def merge(self,l,r):
#         result = []
#         while l and r:
#             if l[0] <= r[0]:
#                 result.append(l.pop(0))
#             else:
#                 result.append(r.pop(0))
#                 self.count += len(l) #计算逆序对数要注意，此时l和r都是已经排好序的了
#         if l:
#             result += l
#         else:
#             result += r
#         return result
#
#     def merge_sort(self,s):
#         if len(s) <= 1: # 例：a = [1],a[:0] =[] 故次处必须是<=1
#             return s #递归边界
#         mid = len(s) // 2
#         l = self.merge_sort(s[:mid])
#         r = self.merge_sort(s[mid:])
#         return self.merge(l,r)


"""归并排序 分而治之 先分再合并"""
# def merge(l,r):
#     result = []
#     while l and r:
#         if l[0] <= r[0]:
#             result.append(l.pop(0))
#         else:
#             result.append(r.pop(0))
#     if l:
#         result += l
#     else:
#         result += r
#     return result
#
# def merge_sort(s):
#     if len(s) <= 1: # 例：a = [1],a[:0] =[] 故次处必须是<=1
#         return s #递归边界
#     mid = len(s) // 2
#     l = merge_sort(s[:mid])
#     r = merge_sort(s[mid:])
#     return merge(l,r)


"""堆排序 建堆 维护堆，堆是完全二叉树。"""
class heap():
    def __init__(self,s):
        self.s = s
        self.heap_size = len(self.s)

    def build_max_heap(self):
        mid = len(self.s) // 2 -1
        for i in range(mid,-1, -1):
            self.maintain_heap(i)
        return self.s

    def maintain_heap(self,i):
        """
        维护大顶堆
        :param i:
        :return:
        """
        left = i*2+1
        right = i*2+2
        largest = i
        if left < self.heap_size and self.s[left] > self.s[largest]:
            largest = left
        if right < self.heap_size and self.s[right] > self.s[largest]:
            largest = right
        if i!= largest:
            self.s[i],self.s[largest] = self.s[largest],self.s[i]
            self.maintain_heap(largest)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heap_size -1 ,0,-1):
            self.s[0],self.s[i] = self.s[i],self.s[0]
            self.heap_size -= 1
            self.maintain_heap(0)
        return self.s

heap = heap(a)
print(heap.build_max_heap())
print(heap.heap_sort())



