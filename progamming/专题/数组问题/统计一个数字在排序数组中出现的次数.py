class Solution:
    def GetNumberOfK(self, data, k):
        #线性复杂度O(n)
        num2cnt = {}
        for num in data:
            if num not in num2cnt.keys():
                num2cnt[num] = 1
            else:
                num2cnt[num] += 1
        return  num2cnt[k]

    def GetNumberOfK2(self,data,k):
        #本质还是利用2分法分别查找第一个k和最后一个k所在的位置
        #2分法查找既可以使用迭代也可以使用递归O(logN)
        first_index = self.FirstK(data,k,0,len(data)-1)
        last_index = self.LastK(data,k,0,len(data)-1)
        return (last_index - first_index)+1

    def FirstK(self,data,k,l,r):
        if l >= r: #递归终止
            return l #返回第一个k的索引位置
        mid = len(data)//2 #此种方式求中点若只有两个数时会是第2个数
        if data[mid] > k:
            return self.FirstK(data,k,l,mid-1)
        elif data[mid] < k:
            return self.FirstK(data,k,mid+1,r)
        elif data[mid] == k:
            if data[mid-1] != k: #当前即为第一个K的位置
                return mid
            elif data[mid-1] == k:
                return self.FirstK(data,k,l,mid-1)

    def LastK(self,data,k,l,r):
        while l < r:
            mid = (l+r) // 2 #此种方式求中点若只有两个数时会是第1个数
            if data[mid] > k:
                r = mid-1
            elif data[mid] < k:
                l = mid + 1
            elif data[mid] == k:
                if data[mid+1] == k: #注意此处有可能超出数组边界
                    l = mid+1
                elif data[mid+1] != k:
                    return mid
        return r

s = Solution()
print(s.GetNumberOfK2([1,3,3,4,4,4,5],4))
