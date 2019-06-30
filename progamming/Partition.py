import random


def Partition(A):
    index =  random.randint(0,len(A)-1)
    print("--index--",index)
    A[index],A[-1] = A[-1],A[index]
    j = -1
    for i in range(len(A)-1):
        if A[i] < A[-1]:
            j += 1
            if j != i:
                A[j],A[i] = A[i],A[j]
    j +=1
    A[j],A[-1] = A[-1],A[j]
    return  j

def quick_sort(A):

    if len(A) > 1: #保证有元素可以进行排序所以应当大于1
        qvoit = Partition(A)
        print('--qvoit--',qvoit)
        print("小于枢轴点的组：",A[0:qvoit])
        print("大于枢轴点的组：",A[qvoit+1:])
        quick_sort(A[0:qvoit]) #此处发生错误，始终记住快排是原地排序，每一次递归排序都是对最初的A进行排序，此处这样写改变了A，由于原地排序，不会有返回值，因此这样做是错误的
        quick_sort(A[qvoit+1:])

A = [5,10,12,3,6,2,9]
quick_sort(A)
print(A)

