def FindContinuousSequence(tsum):
    start = 1
    end = 1
    result = []
    while start <= tsum // 2:
        temp = []
        print("--start--", start)
        print("--end--", end)
        print("--result--", result)
        # while temp_sum <= tsum:
        #     temp_sum = calsum(start, end)
        #     print("--temp_sum--", temp_sum)
        #     if temp_sum == tsum:
        #         for i in range(start, end + 1):
        #             temp.append(i)
        #         result.append(temp)
        #         break
        #     end += 1
        # start = start + 1
        temp_sum = calsum(start, end)
        if temp_sum == tsum:
            for i in range(start, end+1):
                temp.append(i)
            result.append(temp)
            end += 1

        elif temp_sum < tsum:
            end += 1

        elif temp_sum > tsum:
            start += 1

    return result


def calsum(start, end):
    nm = end - start + 1
    return int(nm * start + (nm * (nm - 1) / 2))

print(FindContinuousSequence(15))
