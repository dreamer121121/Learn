def findThird(array):
    #排序，返回array[-3] O(nlogn)
    array.sort()
    return array[-3]

def Partition(nums,l,r):
    pivot = nums[l]
    left,right = [],[]
    for num in nums[l+1:r+1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    new = right+[pivot]+left
    nums[l:r+1] = new
    index = nums.index(pivot)
    return index,nums

def FindThird(array,l,r):
    #利用快速排序的思想O(n)
    index,new_array = Partition(array,l,r)
    if index == 2: #递归终止
        return new_array[index]
    elif index < 2:
        return FindThird(new_array,index+1,r)
    elif index > 2:
       return FindThird(new_array,l,index-1)

# print(findThird([1,2,3,4,3,5]))
print(FindThird([6,1,3,9,2],0,4))


