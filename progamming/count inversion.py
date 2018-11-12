# 暴力破解法
# A = [14, 7, 18, 3, 10, 19, 11, 23, 2, 25, 16, 17]
# count = 0
# trace = []
# for i in range(len(A)-1):
#     start = A[i]
#     for j in range(i + 1, len(A)):
#         if A[j] < start:
#             trace.append((start,A[j]))
#             count += 1
# print(count)
# print(trace)
# print(len(trace))

total = 0


def count(ll, rl):
    result = []
    count = 0
    while len(ll) > 0 and len(rl) > 0:
        if ll[0] > rl[0]:
            count += len(ll)
            result.append(rl.pop(0))
        else:
            result.append(ll.pop(0))
    result += ll
    result += rl
    return count, result


def counting_inversion(A):
    if len(A) == 1:
        return A
    mid = len(A) // 2
    ll = A[:mid]
    rl = A[mid:]
    ll = counting_inversion(ll)
    rl = counting_inversion(rl)
    temp_count, result = count(ll, rl)
    global total
    total += temp_count
    return result


if __name__ == '__main__':
    A = [14, 7, 18, 3, 10, 19, 11, 23, 2, 25, 16, 17]
    result = counting_inversion(A)
    print(result)
    print(total)
