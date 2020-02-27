a = [4,5,7]

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
        print(self.s)
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
        else:
            return

    def heap_sort(self):
        self.build_max_heap()
        # for i in range(self.heap_size -1 ,0,-1):
        #     self.s[0],self.s[i] = self.s[i],self.s[0]
        #     self.heap_size -= 1
        #     self.maintain_heap(0)
        # return self.s

heap = heap(a)
print(heap.heap_sort())


# import random
#
# """快速排序"""
# def quick_sort(b):
#     """快速排序"""
#     if len(b) < 2: #递归边界条件
#         return b
#     # 选取基准，随便选哪个都可以，选中间的便于理解
#     index = random.randint(0,len(b)-1) #随机快排
#     pivot = b[index]
#     # 定义基准值左右两个数列
#     left, right = [], []
#     # 从原始数组中移除基准值
#     b.remove(pivot)
#     for item in b:
#         # 大于基准值放右边
#         if item >= pivot:
#             right.append(item)
#         else:
#             # 小于基准值放左边
#             left.append(item)
#     # 使用迭代进行比较
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# print(quick_sort([5,6,7,3,2,9]))

# """一行实现快速排序"""
# quick_sort = lambda array:array if len(array)<2 else quick_sort([item for item in array[1:] if item < array[0]])+[array[0]]+quick_sort([item for item in array[1:] if item > array[0]])
# print(quick_sort([2,6,3,5,7,1]))
