# class Solution():
#     def merge(self, intervals):
#         result = []
#         origin = intervals
#         for i in range(len(intervals)-1):
#             print("len(intervals)",len(intervals))
#             print('i',i)
#             for j in range(i+1,len(intervals)):
#                 print('j',j)
#                 print(len(intervals))
#                 a,b = intervals[i]
#                 c,d = intervals[j]
#                 if b<c or d<a:
#                     continue
#                 else:
#                     origin.pop(i)
#                     origin.pop(j) #特别注意对origin进行pop()操作时也是对intervals进行操作！！！！可迭代对象的特点！！！
#                     overlap = [min(a,c),max(b,d)]
#                     result.append(overlap)
#         return result+origin
# s = Solution()
# print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
class Solution():
    def merge(self, intervals):
        result = []
        origin = intervals.copy() #此处对列表进行了copy,python重新开辟了一段内存空间存储了跟intervals一样的值，并用origin指向
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                a,b = intervals[i]
                c,d = intervals[j]
                if b<c or d<a:
                    continue
                else:
                    print('i,j', i,j)
                    origin.pop(i)
                    origin.pop(j-1)
                    print(origin)
                    overlap = [min(a,c),max(b,d)]
                    result.append(overlap)
        return result+origin
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
