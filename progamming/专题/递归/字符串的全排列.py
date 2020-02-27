#Input:'abc'
#Output:['abc','bca','acb'] ==》我们需要一个列表来存储所有的path.
# class Solution:
#     def __init__(self):
#         self.result = []
#
#     def Permutation(self, ss):
#         # write code here
#         if not ss: #字符串为空。
#             return None
#         self.Perm(ss,'')
#         unique = list(set(self.result)) #去重
#         unique.sort() #排序
#         return unique
#
#     def Perm(self,ss,path): #递归函数
#         if ss == "":#递归边界条件
#             self.result.append(path)
#             return
#         for i in range(len(ss)):
#             self.Perm(ss[:i]+ss[i+1:],path+ss[i])

class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        path = ""
        self.perm(ss,path)
        unique = list(set(self.result))
        unique = unique.sort()
        return unique
    def perm(self,ss,path):
        if ss == "":
            self.result.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],path+ss[i])
s = Solution()
print(s.Permutation('a'))
print(s.result)