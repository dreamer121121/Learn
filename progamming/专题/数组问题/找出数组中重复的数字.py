class Solution():
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
        #建立哈希表 此做法需要开辟额外的空间
        for num in numbers:
            if dic[num] != 1:
                duplication.append(num)
                return duplication[0]
            else:
                continue
        return False
    def duplicate2(self,numbers,duplication):
        #不用开辟额外的空间，时间复杂度为O(1),空间复杂度O(1)
        for i in range(len(numbers)):
            num = numbers[i]
            if num == i:
                continue
            else:
                if numbers[num] == num:
                    return num
                else:
                    numbers[num],numbers[i] = numbers[i],numbers[num]
        return False
s = Solution()
print(s.duplicate([2,3,1,0,2,5,3],[]))