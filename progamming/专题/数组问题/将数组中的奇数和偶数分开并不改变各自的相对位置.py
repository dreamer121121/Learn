# -*- coding:utf-8 -*-
class Solution():
    #采用插入排序的思想。
    def reOrderArray(self, array):
        # write code here
        odd_index = 0 #记录奇数的部分最后一个位置
        for i in range(len(array)):
            if array[i]%2:#是奇数
                if i != odd_index:
                    for j in range(i,odd_index,-1):
                        array[j],array[j-1] = array[j-1],array[j]
                odd_index += 1
        return array
s = Solution()
print(s.reOrderArray([1,2,3,4,5,6,7,8,9,13,15]))