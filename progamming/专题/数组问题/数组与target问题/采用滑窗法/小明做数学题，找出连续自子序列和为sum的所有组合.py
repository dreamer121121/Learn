#滑窗法
def findContinuousarray(tsum):
    start = 1
    end = 2
    result = []
    while start < end and end < tsum // 2:
        tmp = (end-start+1)*start + (end-start+1)*(end-start)//2
        if tmp == tsum:
            result.append([i for i in range(start,end+1)])
            start += 1
        elif tmp < tsum:
            end += 1
        elif tmp > tsum:
             start += 1
    return result
print(findContinuousarray(100))




