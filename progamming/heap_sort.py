A = [16, 9, 21, 13, 4, 11, 3]
heap_size = len(A)


def Max_heapify(A, i):  # 维护大顶堆O(logn)
    left = 2 * i + 1  # 左孩子节点位置
    right = 2 * i + 2  # 右孩子节点位置
    global heap_size
    if left < heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i

    if right < heap_size and A[right] > A[largest]:
        largest = right

    if i != largest:
        A[largest], A[i] = A[i], A[largest]
        Max_heapify(A, largest)


def build_max_heap(A):
    mid = len(A) // 2 - 1
    for i in range(mid, -1, -1):
        Max_heapify(A, i)


def heap_sort(A):
    build_max_heap(A)  # 构建大顶堆
    print("初始大顶堆A：", A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        global heap_size
        heap_size -= 1
        Max_heapify(A, 0)


if __name__ == '__main__':
    heap_sort(A)
    print("原始A：", A)
    print("排序后的A：", A)
