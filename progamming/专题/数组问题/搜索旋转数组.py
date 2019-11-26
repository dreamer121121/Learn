

def find_rotation_index(nums,l,r):
    if nums[l] < nums[r]:#没有旋转
        return 0
    while l <= r:
        print('l,r',l,r)
        pivot = (l+r)//2
        print('pivot',pivot)
        if nums[pivot]>nums[pivot+1]:#找到旋转点
            return pivot+1
        # elif nums[pivot] < nums [pivot-1]:加不加都可以！
        #     return pivot 加不加都可以
        else:
            if nums[pivot] >= nums[l]:
                l = pivot+1
            else:
                r = pivot-1
    return 0
def search(nums,l,r,target):
    rotation_index = find_rotation_index(nums,l,r)
    print("rotation：",rotation_index)
    # if rotation_index == 0 or rotation_index == len(nums)-1:#没有旋转
    #     pass
    # elif nums[rotation_index] == target:
    #     return rotation_index
    # elif target >= nums[0] and target <= nums[rotation_index-1]:
    #     r = rotation_index -1 #在rotation左边找
    # elif target <= nums[r] and target >= nums[rotation_index+1]:
    #     l = rotation_index #在rotation右边找
    # else:
    #     return -1
    # while l <= r:
    #     mid = (l+r)//2
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] < target:
    #         l = mid+1
    #     elif nums[mid] > target:
    #         r = mid -1
    # return -1



nums= [8,9,2,3,4]
target = 3
print(search(nums,0,len(nums)-1,target))