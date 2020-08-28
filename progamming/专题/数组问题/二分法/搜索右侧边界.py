array = [2]
# int left_bound(int[] nums, int target) {
#     int left = 0, right = nums.length - 1;
#     while (left <= right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] < target) {
#             left = mid + 1;
#         } else if (nums[mid] > target) {
#             right = mid - 1;
#         } else if (nums[mid] == target) {
#             // 别返回，锁定左侧边界
#             right = mid - 1;
#         }
#     }
#     // 最后要检查 left 越界的情况
#     if (left >= nums.length || nums[left] != target)
#         return -1;
#     return left;
# }
def left_bound(array,target):
    if not array:
        return -1
    left = 0
    right = len(array)-1
    while left <= right:
        # mid = left + (right-left) // 2
        mid = (left+right) >> 1 #若(left+right)过大会导致溢出，因此比较保险的方法还是使用上式
        if array[mid] < target:
            left = mid+1
        elif array[mid] > target:
            right = mid-1
        elif array[mid] == target:#不太好理解！
            right = mid-1 #仿佛是将第一个target排除了，但是经过试验发现并没有
    #检查是否越界
    if left >= len(array) or array[left] != target:
        return -1
    return left

def right_bound(array,target):
    if not array:
        return -1
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left + (right-left) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid-1
        elif array[mid] == target:
            left = mid +1
    if right >= len(array) or array[right] != target:
        return -1
    return right

print("result:",left_bound(array,1))

