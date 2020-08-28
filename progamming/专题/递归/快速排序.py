import random
numbers = [2,3,4,7,1,5]
def quick_sort(numbers): #函数定义：输入一个未排序类表，输出一个排好序的类表
    if len(numbers) <= 1: #递归边界
        return numbers
    pivot = random.randint(0,len(numbers)-1)
    P_val = numbers.pop(pivot)
    l = []
    r = []
    for num in numbers:
        if num <= P_val:
            l.append(num)
        else:
            r.append(num)
    return quick_sort(l)+[P_val]+quick_sort(r)
print(quick_sort(numbers))

