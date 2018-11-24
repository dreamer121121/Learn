A = [16, 9, 21, 13, 4, 11, 3]


def Partition(A, p, r):
    povit = A[r]
    l = -1
    i = 0
    while i < r:
        if A[i] < povit:
            l += 1
            A[i], A[l] = A[l], A[i]
        i += 1
    A[l + 1], A[r] = A[r], A[l + 1]
    return l + 1


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    k = Partition(A, p, r)
    if i-1 == k:
        return A[k]
    if i-1 < k:
        return randomized_select(A, p, k - 1, i)
    elif i-1 > k:
        return randomized_select(A, k + 1, r, i)


if __name__ == '__main__':
    print(randomized_select(A, 0, len(A) - 1, 3))
