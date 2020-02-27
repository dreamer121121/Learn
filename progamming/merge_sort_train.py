cnt = 0

def merge(L,R):
    result = []
    while L and R:
        if L[0] <= R[0]:
            result.append(L.pop(0))
        else:
            global cnt
            cnt += len(L)
            result.append(R.pop(0))
    result += L
    result += R
    return result


def merge_sort(array):
    if not array or len(array) == 1: #注意边界条件。
        return array
    mid = len(array) >> 1
    L_array = merge_sort(array[:mid])
    R_array = merge_sort(array[mid:])
    return merge(L_array,R_array)

print(merge_sort([4,3,2,1]))
print(cnt)