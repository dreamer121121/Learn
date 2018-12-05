# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:47:00 2018

@author: outao
"""


def find_max_crossing_subarray(a, center, left, right):
    # 求包含左侧边界的最大值
    maxleftsum = 0
    lsum = 0
    cross_low = 0
    for i in range(center, left - 1, -1):
        lsum += a[i]
        if lsum > maxleftsum:
            maxleftsum = lsum
            cross_low = i  # 记录下左边最小的点的位置

    maxrightsum = 0
    rsum = 0
    cross_high =0
    # 求包含右侧边界的最大值
    for j in range(center + 1, right + 1):
        rsum += a[j]
        if rsum > maxrightsum:
            maxrightsum = rsum
            cross_high = j
    return cross_low, cross_high, maxleftsum + maxrightsum


def maxsubsum(a, left, right):
    if left == right:  # 一直拆分到递归边界开始向上返回
        return left, right, a[left]
    center = (left + right) // 2
    left_low, left_high, maxleftsum = maxsubsum(a, left, center)
    right_low, right_high, maxrightsum = maxsubsum(a, center + 1, right)  # 递归调用
    cross_low, cross_high, maxacrosssum = find_max_crossing_subarray(a, left, center, right)

    # 比较三个值的大小返回最大值和各自的位置

    if maxleftsum >= maxrightsum and maxleftsum >= maxacrosssum:
        return left_low, left_high, maxleftsum
    elif maxrightsum >= maxleftsum and maxrightsum >= maxacrosssum:
        return right_low, right_high, maxrightsum
    elif maxacrosssum >= maxrightsum and maxacrosssum >= maxleftsum:
        return cross_low, cross_high, maxacrosssum


a = [1, -9, 6, 7, -2, 5, 6, -3]
# a = [-1, -2, -3]
print(maxsubsum(a, 0, len(a) - 1))
