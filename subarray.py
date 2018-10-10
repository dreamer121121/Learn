import datetime
import time
import numpy as np
start = time.clock()
print(start)
a = np.arange(-500, 500)
max = 0
trace = []

# O(n3)
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         sum = 0
#         for k in range(i, j + 1):
#             sum += a[k]
#             if sum > max:
#                 max = sum
#                 trace.append((i, j))


# O(n2)
# for i in range(len(a)):
#     sum = 0
#     for j in range(i, len(a)):
#         sum += a[j]
#         if sum > max:
#             max = sum
#             trace.append((i, j))
# end = time.clock()
# print(end)
# during = end-start
# print(during)
# print(max)
# print(trace[-1])

# 递归法


def devide(a):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    li = devide(a[0:middle])
    ri = devide(a[middle+1:])
    return combine(li,ri)

def combine(li,ri):
    pass