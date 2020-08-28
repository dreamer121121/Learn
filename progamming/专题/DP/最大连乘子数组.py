def maxProduct(nums):
    F_max = [1] * (len(nums) + 1)
    F_min = [1] * (len(nums)+1)
    for i in range(1, len(nums) + 1):
        F_max[i] = max(F_max[i-1]*nums[i-1],max(F_min[i - 1] * nums[i-1], nums[i-1]))
        F_min[i] = min(F_min[i-1]*nums[i-1],min(F_max[i-1]*nums[i-1],nums[i-1]))
    print(F_max)
maxProduct([2,3,-2,4])