def FindNumbersWithSum(array, tsum):
    start_index = 0
    end_index = 1
    total_list = []
    while start_index < len(array):
        print("--start_index:--",start_index)
        print("--end_index:--",end_index)
        end_index = start_index+1
        while end_index < len(array):
            temp = []
            temp_sum = array[start_index]+array[end_index]
            print("--temp_sum--",temp_sum)
            if temp_sum == tsum:
                temp.append(array[start_index])
                temp.append(array[end_index])
                total_list.append(temp)
                break
            elif temp_sum > tsum:
                break
            elif temp_sum < tsum:
                end_index += 1
        start_index += 1
    print("--total_list--",total_list)
    if total_list == []:
        return total_list
    else:
        return sorted(total_list)[0]

print(FindNumbersWithSum([1,2,3,4],6))
