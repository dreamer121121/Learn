def indContinuousSequence(tsum):
    result = []
    start = 1
    end = 1
    while start < tsum // 2:
        tmp = []
        tmp_sum = cal_sum(start,end)
        if tmp_sum == tsum:
            for i in range(start,end+1):
                tmp.append(i)
            result.append(tmp)
            start += 1
        elif tmp_sum < tsum:
            end += 1
        elif tmp_sum > tsum:
            start += 1
    return result


def cal_sum(start,end):
    num = end-start+1
    return int(num*start+num*(num-1)/2)

print(indContinuousSequence(100))