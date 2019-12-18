class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        for num in numbers:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
        #建立哈希表
        print('--hash--',dic)
        for num in numbers:
            if dic[num] != 1:
                duplication[0] = num
                return duplication[0]
            else:
                continue
s = Solution()
print(s.duplicate([2,3,1,0,2,5,3],[1]))