import random

def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    #改成随机快排
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


    # pivot = array[r]
    # low = -1
    # for i in range(l, r):
    #     if array[i] < pivot:
    #         low += 1  # 保证low以前的数字都小于pivot值
    #         array[low], array[i] = array[i], array[low]
    # array[low + 1], array[r] = array[r], array[low + 1]
    # return low + 1  # 返回枢轴点的位置


if __name__ == '__main__':
    A = [5, 23, 3, 6, 15]
    quick_sort(A, 0, len(A) - 1)
    print(A)
