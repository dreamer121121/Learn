class Solution():
    # 返回[a,b] 其中ab是出现一次的两个数字

    def FindNumsAppearOnce(self, array):
        #方法一建立哈希表
        cnt = {}
        result = []
        for num in array:
            if num not  in cnt.keys():
                cnt[num] = 1
            else:
                cnt[num] += 1
        for key,value in array.items():
            if value == 1:
                result.append(key)
        return result

    def FindNumsAppearOnce2(self, array):
        #方法二使用位运算
        #本质是对搜索一个数组中独一无二的数的变形
        bitresult = 0
        for num in array:
            bitresult ^= num #此处仍为十进制
        bitresult = list(bin(bitresult).replace('0b','').zfill(8))
        index_1 = bitresult.index('1')
        print(index_1)
        l = []
        r = []
        result = []
        for num in array:
            if bin(num).replace('0b','').zfill(8)[index_1] == '1':
                    l.append(num)
            else:
                r.append(num)
        print(l)
        print(r)
        l_result = self.FindeOnlyone(l)
        r_result = self.FindeOnlyone(r)

        result.append(l_result)
        result.append(r_result)

        return result

    def FindeOnlyone(self,array):
        #一个数与自身按位异或结果为0，一个数与0按位异或结果仍为自身。
        result = 0
        for num in array:
            result ^= num
        return result
s = Solution()
# print(s.FindeOnlyone([1,1,2,2,3]))
print('result:',s.FindNumsAppearOnce2([1,1,2,2,5,5,6,6,7,7,8,9]))




