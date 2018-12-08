A = [12, 5, 7, 3, 1, 45, 22]


def merge(left_array,right_array):
    new_array = []
    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            new_array.append(left_array.pop(0))
        elif right_array[0] <= left_array[0]:
            new_array.append(right_array.pop(0))
    if not left_array:
        new_array += right_array
    if not right_array:
        new_array += left_array
    return new_array


def merge_sort(A, left, right):
    if left == right:
        return A[left]
    mid = (left + right) // 2
    left_array = merge_sort(A[left:mid], left, mid-1)
    right_array = merge_sort(A[mid:right], mid, right)
    return merge(left_array, right_array)


if __name__ == '__main__':
    print(merge_sort(A, 0, len(A) - 1))
