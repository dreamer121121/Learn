def Max_heapify(A, i):
    left = 2 * i + 1
    right = 2*i +2
    if left < len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = right
    if right < len(A) and A[right] > A[i]:
        largest = right
    else:
        largest = i
    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        Max_heapify(A, largest)


def build_max_heap(A):
    mid = len(A) // 2 - 1
    for i in range(mid, -1, -1):
        Max_heapify(A, i)
    print(A)


if __name__ == '__main__':
    A = [16, 9, 21, 13, 4, 11, 3]
    build_max_heap(A)
