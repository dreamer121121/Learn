# coding:utf-8
A = [12, 5, 7, 3, 1, 45, 22]
for i in range(1, len(A)):
    print(A)
    key = A[i]
    print("取出：%d" % key)
    for j in range(i, 0, -1):
        print("A[j-1]:%d"%A[j-1])
        if A[j - 1] > key:
            A[j] = A[j - 1]
            A[j - 1] = key
print(A)
