def threeSum(nums,target):
    """
    基本思路：
    1.排序
    2.当前元素num[i] 当前元素右半部分从num[i+1]开始 若num[i]+num[L]+num[R] > 0 则以num[i]为最小值的三个数相加不可能为0，终止此循环
    :param nums:
    :return:
    """
    nums.sort()
    length = len(nums)
    min_d = float('inf')
    sum = 0
    for i in range(length):
        current = nums[i]
        L= i+1
        R = length-1
        while L < R:
            sum = current + nums[L] + nums[R]
            distance = abs(sum-target)
            if distance < min_d:
                min_d = distance
            if sum < target:
                L += 1
            elif sum > target:
                R -= 1
    return sum
print(threeSum([-1,2,1,-4],target=1))
