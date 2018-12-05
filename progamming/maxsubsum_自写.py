# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:47:00 2018

@author: outao
"""


def max_crossing_sum(a, left, center, right):
    # 求包含左侧边界的最大值
    maxleftbordersum = 0
    leftbordersum = 0
    for i in range(center, left - 1, -1):
        leftbordersum += a[i]
        if leftbordersum > maxleftbordersum:
            maxleftbordersum = leftbordersum
    # 求包含右侧边界的最大值
    maxrightbordersum = 0
    rightbordersum = 0
    for j in range(center + 1, right + 1):
        rightbordersum += a[j]
        if rightbordersum > maxrightbordersum:
            maxrightbordersum = rightbordersum
    maxacrosssum = maxleftbordersum + maxrightbordersum
    return maxacrosssum


def maxsubsum(a, left, right):
    trace = []
    if left == right:  # 递归边界
        return a[left]
    center = (left + right) // 2
    maxleftsum = maxsubsum(a, left, center)
    maxrightsum = maxsubsum(a, center + 1, right)  # 递归调用
    maxcross, i, j = max_crossing_sum(a, left, center, right)
    result = max(maxleftsum, maxrightsum, maxcross)
    trace.append((i, j))
    return result


if __name__ == "__main__":
    a = [1, -9, 6, 7, -2, 5, 6, -3]
    # a = [-1, -2, -3]
    result = maxsubsum(a, 0, len(a) - 1)
    print(result)





# data_reuse实现最大连续子数组
# max_sum = 0
# trace = []
# for i in range(len(a)):
#     sum = 0
#     for j in range(i, len(a)):
#         sum += a[j]
#         if sum > max_sum:
#             max_sum = sum
#             trace.append((i, j))
# print(trace[-1])
# print(max_sum)
