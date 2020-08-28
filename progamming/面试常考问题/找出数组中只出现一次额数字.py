#题目：
#一个数组中只有一个数字只出现了一次，其他数组出现了两次,找出只出现一次的数字
#方法一：遍历数组使用hash表存储数字的个数，再找出value值唯一的数字
#算法复杂度分析：
#时间复杂度O(N),空间复杂度O(n)
#方法二：#使用异或运算
#
# def findOnly(array):
#     res = 0
#     for num in array:
#         res ^= num
#     return res
#
# array = [1,2,1,2,3]
# print(findOnly(array))

#变式题，数组中包含两个只出现了一次的数，其余数字全部出现了两次
def findOnly2(array):
    """
    0与任何数异或都是这个数本身
    任何数与自身异或都是0
    :param array:
    :return:
    """
    res = 0
    for num in array:
        res ^= num
    index = findFirstIndex(res)
    num_0 = 0
    num_1 = 0
    for num in array:
        if judge(num,index):
            num_1 ^= num
        else:
            num_0 ^= num
    return [num_0,num_1]

def findFirstIndex(num):
    index = 0
    while num & 1 == 0:
        num >> 1
        index += 1
    return index

def judge(num,index):
    num = num >> index
    return (num & 1)

array = [1,1,2,2,3,3,4,9]
print(findOnly2(array))





