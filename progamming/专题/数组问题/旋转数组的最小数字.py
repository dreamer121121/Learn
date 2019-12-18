class Solution():
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        #方法1：遍历一遍数组O(n)
        min_num = float('inf')
        for num in rotateArray:
            if num < min_num:
                min_num = num
            else:
                continue
        return min_num
    def minNumberInRotateArray2(self, rotateArray):
        #二分法
        def search(array,l,r):
            # while l < r: 迭代
            #     mid = (l+r)//2
            #     mid_num = array[mid]
            #     if mid_num > array[r]:
            #         l = mid + 1
            #     elif mid_num < array[r]:
            #         r = mid
            #     elif mid_num == array[r]:
            #         r -= 1
            # return array[l]

            #递归
            if l >= r:
                return array[l]
            mid = (l+r)//2
            if array[mid] > array[r]:
                return search(array,mid+1,r)
            elif array[mid] < array[r]:
                return search(array,l,mid)
            else:
                return search(array,l,r-1)
        return search(rotateArray,0,len(rotateArray)-1)

s = Solution()
# print(s.minNumberInRotateArray([3,4,5,1,2]))
print(s.minNumberInRotateArray2([3,4,5,1,2]))


