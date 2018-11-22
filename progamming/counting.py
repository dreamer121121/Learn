A = [16, 9, 21, 13, 4, 11, 3]
B = []
C = []


def counting_sort(A):
    for i in range(23):
        C.append(0)
    print(C)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1  # 计数排序的核心
        B.append(0)
    print(C)
    for i in range(1, len(C)-1):
        C[i] = C[i - 1] + C[i]
    print(C)
    for j in range(len(A) - 1, -1, -1):  # 遍历数组A一次插入数租B中
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


if __name__ == '__main__':
    counting_sort(A)
    print(B)
