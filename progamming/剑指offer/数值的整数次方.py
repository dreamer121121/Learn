#全面但不高效的解法
error_flag = False #异常标志位
def Power(base,exponent):
# 考虑底数为0，指数为正
    if base == 0.0 and exponent < 0:
        error_flag = True
        return  0.0

    absexponent = abs(exponent)
    temp = powerwithabsexponent(base,absexponent)
    if exponent < 0:
        return 1/temp
    else:
        return temp

def powerwithabsexponent(base,absexponent):

    result = 1.0
    if base == 0.0 and absexponent == 0:
        error_flag = True
        return 0.0

    for i in range(absexponent):
        result *= base
    return result

print(Power(1,0))
