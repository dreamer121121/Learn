# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)
#
# #编写函数求Cn^m
# # def select(n,m):
# #     if n == m or m ==0:
# #         return 1
# #     return select(n-1,m)+select(n-1,m-1)
# #
# # def solution(n,m):
# #     return select(n,m)*select(m,2)
# # # print(solution(10,10))
#
# import math
#
# # def rec(n, m):
# #     if m == n:
# #         return 1
# #     elif m == 1:
# #         return n
# #     else:
# #         return rec(n - 1, m - 1) + rec(n - 1, m)
#
# # print(rec(n, m))
#
# def power(x,y):     #求x的y次方
#     p = 100000007
#     res = 1
#     while y:
#         if y % 2 != 0:
#             res *= (x%p)
#         y >>= 1
#         x *= (x%p)
#     return res
#
# def solution(n,m):
#     p = 100000007
#     a = (math.factorial(n))
#     b = (power(math.factorial(m),(p-2)))
#     c = (power(math.factorial(n-m),(p-2)))
#     return a*b*c%p
# print(solution(10,10))

# def pow(n):
#     res=1
#     base=2
#     while n:
#         if n&1:
#             res=(res*base)%(10**9+7)
#         base=(base*base)%(10**9+7)
#         n>>=1
#     return res
# print(pow(3))
#
# def get_value(n):
#     if n == 1:
#         return n
#     else:
#         return n * get_value(n - 1)
#
#
# def gen_last_value(n, m):
#     first = get_value(n)
#     second = get_value(m)
#     third = get_value((n - m))
#     return first / (second * third)
# print(gen_last_value(10,10))

# if __name__ == "__main__":
#     ans = 0
#     n = 10
#     for i in range(n):
#         people = i+1
#         if people == 1:
#             ans += n
#             print(ans)
#         else:
#             res = solution(n,people)
#             ans += res * people
#     ans %= 10000000007
#     print(ans)

def pow(n):
    res=1
    base=2
    while n:
        if n&1:
            res=(res*base)%(10**9+7)
        base=(base*base)%(10**9+7)
        n>>=1
    return res

if __name__ == "__main__":
    n = 10
    ans = n*pow(n-1)%10000000007
    print(ans)
