def MoreThanHalfNum_Solution(numbers):
    # write code here
    # 采用O(2*n)时间复杂度
    flag = 0
    target_num = 0
    index = 0
    while index < len(numbers):
        if flag == 0:
            target_num = numbers[index]
            flag = 1
        elif numbers[index] == target_num:
            flag += 1
        elif numbers[index] != target_num:
            flag -= 1
        index += 1
    return target_num
