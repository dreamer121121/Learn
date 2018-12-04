A = 'aaba'
B = 'abaa'


def judge(a, b, c):
    # 考虑递归边界
    if c == 1:
        if A[a] == B[b]:
            return True
        else:
            return False
    if A[a:a + c] == B[b:b + c]:
        return True
    if judge(a, b, c // 2) and judge(a + c // 2, b + c // 2, c // 2):
        return True
    if judge(a, b + c // 2, c // 2) and judge(a + c // 2, b, c // 2):
        return True
    return False


print(judge(0, 0, len(A)))
