# brute algorithm 算法复杂度为O(n^2)容易误解为O(n^3)
a = [1, 2, 3]
b = [3, 2, 2]
# c = []
# sum = 0
# count = 0
# for k in range(len(a + b) - 1):
#     sum = 0
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if i + j == k:
#                 sum += a[i] * b[j]
#                 count += 1
#     c.append(sum)
# # print(c)
# print(count)

# Devide and conquer

def convolution(A, B):
    mid = len(A) // 2
    A0 = A[0:mid]
    A1 = A[mid:len(A) - 1]
    B0 = B[0:mid]
    B1 = B[mid:len(B) - 1]
    U = convolution(A0, B0)
    V = convolution(A0, B1)
    W = convolution(A1, B0)
    Z = convolution(A1, B1)
    return U + V + W + Z


print(convolution(a, b))
