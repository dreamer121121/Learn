#最简单的思路
# def GetUglyNumber_Solution(index):
#     if index == 1:
#         return 1
#     count = 1
#     num = 1
#     while count < index:
#         num += 1
#         if judge(num):
#             count += 1
#     return num
#
#
# def judge(num):
#     standard = [2, 3, 5]
#     all_prime = list(devide(num))
#     print("--all_prime--",all_prime)
#     for each in all_prime:
#         if each not in standard:
#             return False
#     return True
#
#     # write code here
#
#
# def devide(n):
#     result = []
#     prime = int(2)
#     while (n >= prime):
#         k = n % prime
#         if (k == 0):
#             n = n / prime
#             result.append(prime)
#         else:
#             prime = prime + 1
#     return set(result)
#
# print(GetUglyNumber_Solution(9))

def Min(n2,n3,n5):
    """
    返回最小的
    :param n2:
    :param n3:
    :param n5:
    :return:
    """
    return min(n2,n3,n5)


#解法二用空间换时间
import numpy as np
def GetUglyNumber_Solution(index):
    Ugly_array = [0]*index
    Ugly_array[0] = 1
    P2 = 0
    P3 = 0
    P5 = 0
    next_ugly_index = 1
    while next_ugly_index < index:
        min = Min(Ugly_array[P2]*2,Ugly_array[P3]*3,Ugly_array[P5]*5)
        Ugly_array[next_ugly_index] = min
        while Ugly_array[P2]*2 <= Ugly_array[next_ugly_index]:
            P2 += 1
        while Ugly_array[P3] *3 <= Ugly_array[next_ugly_index]:
            P3 += 1
        while Ugly_array[P5] *5 <= Ugly_array[next_ugly_index]:
            P5 += 1
        next_ugly_index += 1
    print(Ugly_array)
    return Ugly_array[next_ugly_index-1]

print(GetUglyNumber_Solution(11))

