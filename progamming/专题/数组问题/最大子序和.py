a = [2,3,1,5,4,-1,-2]

def maxsubsum(sequence): #返回一个序列的最大连续子序和（相信他能实现）
    if not sequence:
        return 0
    elif len(sequence) == 1:
        return sequence[0]
    mid = len(sequence) >> 1
    left_maxsum = maxsubsum(sequence[:mid])
    right_maxsum = maxsubsum(sequence[mid:])
    mid_maxsum = midmaxsum(sequence)
    return max(left_maxsum,right_maxsum,mid_maxsum)

def midmaxsum(sequence):
    mid = len(sequence)>>1
    max_left = -float("inf")
    tmp = 0
    for i in range(mid,-1,-1):
        tmp += sequence[i]
        if max_left < tmp:
            max_left = tmp
    max_right = -float('inf')
    tmp = 0
    for j in range(mid+1,len(sequence)):
        tmp += sequence[j]
        if tmp > max_right:
            max_right = tmp
    return max_right+max_left

print(maxsubsum(a))






