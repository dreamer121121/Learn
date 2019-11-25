def fourSum(nums,target):
    nums.sort()
    print(nums)
    result = []
    for i in range(len(nums)):
        if i == 0 or nums[i] > nums[i-1]:
            j = i+1
            while j < len(nums)-1:
                if j == i+1 or nums[j] > nums[j-1]:
                    L = j+1
                    R = len(nums)-1
                    while L < R:
                        sum = nums[i]+nums[j]+nums[L]+nums[R]
                        if sum == target:
                            result.append([nums[i],nums[j],nums[L],nums[R]])
                            L += 1
                            R -= 1
                            while L < R and nums[L] == nums[L-1]:
                                L += 1
                            while L < R and nums[R] == nums[R+1]:
                                R -= 1
                        elif sum < target:
                            L +=1
                        elif sum > target:
                            R -= 1
                j += 1
    return result

nums = [-1, 0, 1, 2, -1,-4]
target = -1
print(fourSum(nums,target))