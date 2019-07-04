
#
# def find_max_crossing_subarray(A,low,mid,high):
#     leftmaxsum = -float("Inf")
#     max_left = -1
#     max_right = -1
#     sum = 0
#     for i in range(mid,low-1,-1): #注意此处使用range要格外注意左闭右开的性质，此处必须要low-1才能取到
#         sum += A[i]
#         if sum > leftmaxsum:
#             max_left = i
#             leftmaxsum = sum
#     rightmaxsum = -float("Inf")
#     sum = 0
#     for j in range(mid+1,high+1): #注意此处同上，要格外注意high+1
#         sum += A[j]
#         if sum > rightmaxsum:
#             max_right = j
#             rightmaxsum = sum
#     return max_left,max_right,leftmaxsum + rightmaxsum
#
# def find_maximum_subarray(A,low,high):
#     if low == high:
#         return low,high,A[low]
#     else:
#         mid = (low+high)//2
#         left_low,left_high,maxleftsum = find_maximum_subarray(A,low,mid)
#         right_low,right_high,maxrightsum = find_maximum_subarray(A,mid+1,high)
#         cross_low,cross_high,crosssum = find_max_crossing_subarray(A,low,mid,high)
#         result = max(maxleftsum,maxrightsum,crosssum)
#         if result == maxleftsum:
#             print("--取左边的--",result)
#             return left_low,left_high,result
#         elif result == maxrightsum:
#             print("--取右边的--",result)
#             return right_low,right_high,result
#         elif result == crosssum:
#             print("--取中间的--",result)
#             return cross_low,cross_high,result
#
# print("--result--",find_maximum_subarray([6,-3,-2,7,-15,1,2,2],0,7))
def FindGreatestSumOfSubArray(array):
    # write code here
    low = 0
    high = len(array) - 1
    if low == high:
        return array[low]
    else:
        mid = (low + high) // 2
        leftmaxsum = FindGreatestSumOfSubArray(array[low:mid + 1])
        rightmaxsum = FindGreatestSumOfSubArray(array[mid + 1:])
        crossmaxsum = findcrossmaxsum(array, low, mid, high)
        return  max(leftmaxsum,rightmaxsum,crossmaxsum)


def findcrossmaxsum(array, low, mid, high):
    leftmaxsum = -float("Inf")
    sum = 0
    for i in range(mid, low - 1, -1):  # 注意此处使用range要格外注意左闭右开的性质，此处必须要low-1才能取到
        sum += array[i]
        if sum > leftmaxsum:
            leftmaxsum = sum
    rightmaxsum = -float("Inf")
    sum = 0
    for j in range(mid + 1, high + 1):  # 注意此处同上，要格外注意high+1
        sum += array[j]
        if sum > rightmaxsum:
            rightmaxsum = sum
    return leftmaxsum + rightmaxsum


print("--result--",FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))