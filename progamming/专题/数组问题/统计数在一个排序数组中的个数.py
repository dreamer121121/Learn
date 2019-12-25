# # 方法一：O (n)
# def count_K(data,k):
#     return list(data).count(k)


def GetFirstK(data,k,start,end):
    """
    原地递归操作
    :param data:
    :param k:
    :param start:
    :param end:
    :return:
    """
    if start>end:
        return -1
    mid_index = (start+end)//2
    mid_value = data[mid_index]
    if mid_value == k:
        if (mid_index > 0 and data[mid_index -1] != k) or (mid_index == 0):
            return mid_index
        else:
            end = mid_index - 1
    elif mid_value < k:
        start = mid_index + 1
    elif mid_value >k:
        end = mid_index - 1
    return GetFirstK(data,k,start,end)

def GetLastK(data,k,start,end):
    if start > end:
        return -1
    mid_index = (start + end)//2
    mid_value = data[mid_index]
    if mid_value == k:
        if (mid_index<len(data)-1 and data[mid_index+1] != k) or (mid_index == len(data)-1):
            return mid_index
        else:
            start = mid_index+1
    elif mid_value > k:
        end = mid_index - 1
    elif mid_value < k:
        start = mid_index+1
    return GetLastK(data,k,start,end)

#方法二：
def count_K(data,k,start,end):
    FirstKindex = GetFirstK(data,k,start,end)
    LastKindex = GetLastK(data,k,start,end)
    print("--firstkindex--",FirstKindex)
    print("--lastkindex--",LastKindex)
    if LastKindex >=0 and FirstKindex >=0:
        count = LastKindex - FirstKindex+1
        return count
    else:
        return 0
print(count_K([3,3,3,3],3,0,3))