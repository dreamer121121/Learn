"""
迭代公式：Xn+1 = (1-1/m)Xn+num*Xn/mXn^m
"""

# print(x_power_y(3,2))

def sqrtn(num,m):
    x = num // 2
    iters = 500
    while iters:
        x = (1-1.0/m)*x+(num)/(m*(x**(m-1)))
        iters -= 1
    return x
print(sqrtn(2,2))

def x_power_y(num,n):
    """定义函数：求num的n次方"""
    if n == 0:
        return 1
    return num * x_power_y(num,n-1)