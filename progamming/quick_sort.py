import random




A = [5,6,2,9,4,1,3,8,12,32,6,50,26,100,99,70,88,656,66]

def Partition(array,start,end):
    i = -1
    j = 0
    random_pivot = random.randint(start,end+1)
    pivot_value = array[random_pivot]
    array[random_pivot],array[end] = array[end],array[random_pivot]
    while j < end+1:
        if array[j] < pivot_value:
            i+=1
            if i != j:
                array[i],array[j] = array[j],array[i]
        j += 1
    pivot = i+1
    array[pivot],array[end] = array[end],array[pivot]

    return pivot

def Quick_sort(array,l,r):
    if l < r: #递归边界
        pivot = Partition(array,l,r)
        Quick_sort(array,l,pivot-1)
        Quick_sort(array,pivot+1,r)

Quick_sort(A,0,len(A)-1)
print(A)
