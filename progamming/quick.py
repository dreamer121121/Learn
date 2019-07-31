import random
"""
此代码的思路上不明朗,有错误！！！！！
"""
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    #改成随机快排
    print("--len(array)--",len(array))
    index = random.randint(0,len(array)-1)
    array[index],array[-1] = array[-1],array[index]
    j = -1
    for i in range(len(array)):
        if array[i] < array[-1]:
            j += 1
            if j != i:
                array[i],array[j] = array[j],array[i]
    j += 1
    array[j],array[-1] = array[-1],array[j]
    return j

if __name__ == '__main__':
    A = [5,6,2,9,4,1,3,8,12,32,6,50,26]
    quick_sort(A, 0, len(A) - 1)
    print(A)
