def Add(num1, num2):
    jinwei = -1
    sum = 0
    while jinwei != 0:
        sum = num1^num2
        jinwei = (num1&num2)<<1
        num1 = sum
        num2 = jinwei
    return sum
    # write code here
print(Add(1,2))