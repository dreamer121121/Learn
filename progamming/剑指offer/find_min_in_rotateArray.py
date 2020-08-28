def minNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    if len(rotateArray) == 1:
        return rotateArray[0]
    else:
        left = 0    if int(right-left) == 1:
        right = len(rotateArray) - 1
        while rotateArray[left] >= rotateArray[right]:

                return rotateArray[right]
            mid = (left + right) // 2
            """关键部分"""
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
            """关键部分"""
        return rotateArray[left]

print(minNumberInRotateArray([6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,
                              9170,9359,9719,9895,9896,9913,9962,154,293,334,492,
                              1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,
                              3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,
                              5725,6300,6335]))


# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         """
#         :type rotateArray: List[int]
#         :rtype: int
#         """
#         if rotateArray == None or len(rotateArray) == 0:
#             return 0
#         if rotateArray[0] < rotateArray[-1]:
#             return rotateArray[0]
#         left = 0
#         right = len(rotateArray) - 1
#         while left <= right:
#             if right - left == 1:
#                 mid = right
#                 break
#             mid = (left + right) / 2
#             if rotateArray[mid] == rotateArray[left] == rotateArray[right]:
#                 return self.ordersearch(rotateArray, left, right)
#             if rotateArray[right] <= rotateArray[mid]:
#                 left = mid
#             elif rotateArray[mid] <= rotateArray[right]:
#                 right = mid
#         return rotateArray[mid]
#     def ordersearch(self, A, left, right):
#         res = A[left]
#         for i in range(left, right + 1):
#             res = min(res, A[i])
#         return res