#问题转化为：在nums1中寻找一个i,使得以下两个条件成立：
#1.红线左边的数都小于红线右边的数
#2.(1).len(nums1+nums2) 为奇数时：size_left = size_right + 1
#. (2)len(nums1+nums2) 为偶数时：size_left = size_right
#3.i+j = size_left
a = [1,3,5,6]
b = [2,4,6,8]

def findmidof2list(num1,num2):
    if len(num1) > len(num2):
        num1,num2 = num2,num1
    m = len(num1)
    n = len(num2)
    left = 0
    right = m
    left_total = (m+n+1) >> 1 #粉红色部分总的个数 ?
    while left < right:
        i = (left+right) >> 1
        j = left_total-i

        if num2[j-1] > num1[i]:
            left = i+1
        else:
            right = i
    i = left
    j = left_total - i

    num1_left_max = float('-inf') if i == 0 else num1[i-1]
    num1_right_min = float('inf') if i == m else num1[i]
    num2_left_max = float('-inf') if j== 0 else num2[j-1]
    num2_right_min = float('inf') if j==n else num2[j]

    if (m+n) %2 != 0:
        #奇数
        return max(num1_left_max,num2_left_max)
    else:
        #偶数
        return (max(num1_left_max,num2_left_max)+min(num1_right_min,num2_right_min))/2.0



print(findmidof2list(a,b))

