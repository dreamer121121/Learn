# coding=utf-8
"""原地删除有序数组中重复的数字，不能使用额外的空间，
请使用o(1)的额外空间度来完成，返回删除后新数组的长度"""
def del_repete(nums):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]
    return nums[:slow+1]

nums = [1,2,3,3,5,5,5,5,5,6]
print(del_repete(nums))
