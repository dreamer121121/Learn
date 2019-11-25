def searchRange(nums,target):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] == target:
            mid_l = mid-1
            mid_r = mid+1
            while mid_l >=l and nums[mid_l] == nums[mid]:
                mid_l -= 1
            while mid_r <=r and nums[mid_r] == nums[mid]:
                mid_r += 1
            return [mid_l+1,mid_r-1]
        elif nums[mid] > target:
            r = mid -1
        elif nums[mid] < target:
            l = mid +1
    return [-1,-1]

print(searchRange([5,7,7,8,8,10],8))

