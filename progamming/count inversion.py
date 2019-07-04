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
        return 0,A
    mid = len(A) // 2
    ll = A[:mid]
    rl = A[mid:]
    lastlCount,ll = counting_inversion(ll)
    lastrCount,rl = counting_inversion(rl)
    current_count, result = count(ll, rl)
    return current_count+lastlCount+lastrCount,result


if __name__ == '__main__':
    A = [364,637,341,406,747,995,234,971,571,219,993,
          407,416,366,315,301,601,650,418,355,460,505,
          360,965,516,648,727,667,465,849,455,181,486,
          149,588,233,144,174,557,67,746,550,474,162,268,
          142,463,221,882,576,604,739,288,569,256,936,275,
          401,497,82,935,983,583,523,697,478,147,795,380,973,
          958,115,773,870,259,655,446,863,735,784,3,671,433,
          630,425,930,64,266,235,187,284,665,874,80,45,848,38,
          811,267,575]
    count,result = counting_inversion(A)
    print(count)
