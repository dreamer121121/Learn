#方法一:思路最简单求出整数的补码，然后统计1的个数
#此题若用python求解要注意：
#在刷题过程中，发现Python有一个和其他语言完全不一样的地方，
# 就是对负数的二进制表示。Python里的数是无所谓Overflow的，
# 即没有位数限制，因此也就无所谓补码，因为补码都是相对于位数来说的，
# 32位补码和16位补码，肯定是不一样的。但是这样就导致了一个问题，
# 就是无法直接得到32位二进制补码。
#自己实现32位补码用以表示负数的二进制。


# def solution(n):
#     count = 0
#     binary = bin(abs(n))
#     binary = binary.split("b")[1]
#     for i in range(len(binary)):
#         if binary[i] == "1":
#             count +=1
#     return  count
# print(solution(-9))

def NumberOf1(n):
    # write code here
    count = 0
    binary = (bin(((1 << 32) - 1) & n)[2:]).zfill(32)
    print(binary)
    for i in range(len(binary)):
        if binary[i] == "1":
            count += 1
    return count

print(NumberOf1(1))

#解法二
# def NumberOf1(n):
#     # write code here
#     return sum([(n >> i & 1) for i in range(0, 32)])
# print(NumberOf1(-1))


def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)


print(intToBin32(-1))