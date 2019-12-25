# -*- coding:utf-8 -*-
from functools import reduce
class Solution():
    def multiply(self, A):
        #O(N2,时间复杂度很高)
        B = []
        length = len(A)
        for i in range(length):
            tmp = A.copy() #深拷贝
            tmp.pop(i)
            B.append(reduce(lambda x,y:x*y,tmp))
        return B
    def multiply2(self, A):
        B = []
        length = len(A)
        for i in range(length):
            #计算B[i]的左边的乘积
            if i == 0:
                B.append(1)
            else:
                B.append(B[i-1]*A[i-1])
        tmp = 1
        for j in range(length-1,-1,-1):
            if j == length-1:
                tmp = 1
            else:
                tmp *= A[j+1]
            B[j] *= tmp
        return B



s = Solution()
print(s.multiply([1,2,3,4]))

