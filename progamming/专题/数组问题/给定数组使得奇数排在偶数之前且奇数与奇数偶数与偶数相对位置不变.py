class Solution:
    def reOrderArray(self, array):
        # write code here
        #方法一O(n)
        odd = []
        even = []
        for num in array:
            if num%2:
                odd.append(num)
            else:
                even.append(num)
        return odd+even

    def reOrderArray2(self, array):
        #稳定性排序，借助插入排序思想
        length = len(array)
        k = 0
        for i in range(length):
            if array[i]%2:#发现奇数
                j = i
                while j > k:
                    array[j],array[j-1] = array[j-1],array[j]
                    j-=1
                k += 1
        return array
s = Solution()
print(s.reOrderArray2([3,4,5,7,6]))