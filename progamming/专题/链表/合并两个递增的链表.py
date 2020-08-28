# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         if not pHead1:
#             return pHead2
#         if not pHead2:
#             return pHead1
#         if pHead1.val <= pHead2.val:
#             pHead1.next = self.Merge(pHead1.next,pHead2)
#             return pHead1
#         else:
#             pHead2.next = self.Merge(pHead1,pHead2.next)
#             return pHead2

