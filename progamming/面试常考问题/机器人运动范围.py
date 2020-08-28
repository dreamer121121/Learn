def sum_num(num):
    sum = 0
    while num:
        sum += num % 10
        num = num // 10
    return sum
print(sum_num(45))
