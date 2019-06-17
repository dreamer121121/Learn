import datetime
import time
import numpy as np

'''
# start = time.clock()
# print(start)
# a = np.arange(-500, 500)
# max = 0
# trace = []

# O(n3)
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         sum = 0
#         for k in range(i, j + 1):
#             sum += a[k]
#             if sum > max:
#                 max = sum
#                 trace.append((i, j))
'''

# O(n2)
# a = [1, -9, 6, 7, -2, 5, 6, -3]
# max=0
# trace=[]
# for i in range(len(a)):
#     sum = 0
#     for j in range(i, len(a)):
#         sum += a[j]
#         if sum > max:
#             max = sum
#             trace.append((i, j))
#
# print(max)
# print(trace[-1])


# 递归法求最大子数组


def MaxCrossSubArray(A, low, mid, high):
    LeftMaxSum = A[mid]
    leftSum = A[mid]
    leftIndex = mid
    for i in range(mid - 1, low - 1, -1):
        leftSum = leftSum + A[i]
        if leftSum > LeftMaxSum:
            LeftMaxSum = leftSum
            leftIndex = i
    rightMaxSum = 0
    rightSum = 0
    rightIndex = mid
    for i in range(mid + 1, high + 1):
        rightSum += A[i]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
            rightIndex = i
    MaxSum = LeftMaxSum + rightMaxSum
    return (MaxSum, leftIndex, rightIndex)


def MaxSubArray(A, low, high):
    if low == high:
        return (A[low], low, high)
    mid = (low + high) // 2
    Left = MaxSubArray(A, low, mid)  # 开始递归了一直要将数组分解到单个后才能继续向下进行
    Cross = MaxCrossSubArray(A, low, mid, high)
    Right = MaxSubArray(A, mid + 1, high)
    List = [Left, Cross, Right]
    result = sorted(List, key=lambda list: list[0], reverse=True)
    return result[0]


a = [6,-3,-2,7,-15,1,2,2]
print(MaxSubArray(a, 0, len(a)-1))





