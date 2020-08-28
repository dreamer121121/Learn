def findnumberofK(nums,k):
    first = getFirst(nums,k)
    last = getLast(nums,k)
    return (last-first)+1

def getFirst(nums,k):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] > k:
            r = mid -1
        elif nums[mid] < k:
            l = mid + 1
        else:
            if nums[mid-1] == k:
                r = mid -1
            elif nums[mid-1] != k:
                return mid
    return l

def getLast(nums,k):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r) // 2
        if nums[mid] > k:
            r = mid - 1
        elif nums[mid] < k:
            l = mid + 1
        else:
            if nums[mid+1] == k:
                l = mid + 1
            else:
                return mid
    return l

print(findnumberofK([1,3,3,4,4,4,5],5))

