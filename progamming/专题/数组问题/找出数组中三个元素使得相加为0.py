def threeSum(nums):
    """
    基本思路：
    1.排序
    2.当前元素num[i] 当前元素右半部分从num[i+1]开始 若num[i]+num[L]+num[R] > 0 则以num[i]为最小值的三个数相加不可能为0，终止此循环
    :param nums:
    :return:
    """
    nums.sort()
    print(nums)
    length = len(nums)
    result = []
    for i in range(length):
        current = nums[i]
        L= i+1
        R = length-1
        if current > 0:
            continue
        if i > 0:
            if current == nums[i - 1]:
                continue
        while L < R:
            sum = current + nums[L] + nums[R]
            if sum == 0: #找到一个解
               result.append([current,nums[L],nums[R]])

               """去重"""
               while L < R and nums[L] == nums[L+1]:
                   L +=1
               while L < R and nums[R] == nums[R-1]:
                   R -= 1
               """"""
               L += 1
               R -= 1
            if  sum > 0 :
                R-=1
            if sum < 0:
                L +=1
    return result
print(threeSum([0,0,0]))









