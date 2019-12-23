class Solution():
    def __init__(self):
        self.inverse_cnt = 0
    def merge(self,l_array,r_array):
        result = []
        length_l = len(l_array)
        length_r = len(r_array)
        i = 0
        j = 0
        while i<length_l and j < length_r:
            if l_array[i] <= r_array[j]:
                result.append(l_array[i])
                i += 1
            else:
                result.append(r_array[j])
                self.inverse_cnt += len(l_array[i:]) #计算逆序对数时紧盯右边的数组
                j += 1
        if i < length_l:
            result += l_array[i:]
        elif j < length_r:
            result += r_array[j:]
        return result

    def InversePairs(self, data):
        def merg_sort(data):
            if len(data) < 2:  #递归终止
                return data
            mid = len(data)//2
            l_array = data[:mid]
            r_array = data[mid:]
            l = merg_sort(l_array)
            r = merg_sort(r_array)
            return self.merge(l,r)
        merg_sort(data)
        return self.inverse_cnt
s = Solution()
print(s.InversePairs([2,1,5,7,4,0]))






