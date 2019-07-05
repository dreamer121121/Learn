# -*- coding:utf-8 -*-
def IsContinuous(numbers):
    # write code here
    flag = True
    if 0 not in numbers:
        numbers.sort()
        for i in range(len(numbers)-1):
            if numbers[i+1] - numbers[i] != 1:
                flag = False
                break
    elif 0 in numbers:
        num_0 = numbers.count(0)
        while 0 in numbers:
            numbers.remove(0)
        numbers.sort()
        distance = 0
        for i in range(len(numbers)-1):
            neibor = numbers[i+1]-numbers[i]
            if neibor == 0:
                flag = False
                break
            distance += numbers[i+1]-numbers[i]
        if distance - len(numbers) + 1 > num_0:
            flag = False
    return flag
print(IsContinuous([1,3,2,6,4]))