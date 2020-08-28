#滑窗法要问的4个问题：
"""
1、当移动right扩大窗口，即加入字符时，应该更新哪些数据？

2、什么条件下，窗口应该暂停扩大，开始移动left缩小窗口？

3、当移动left缩小窗口，即移出字符时，应该更新哪些数据？

4、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？

"""


S= "EBBANCF"
T = "AB"
#
# def slidwindow(S,T):
#     window = {}
#     need = {}
#     left = 0
#     right = 0
#     valid = 0 #用于指示是否该缩减窗口了，当valid == len(need)
#     #用于记录最终的结果
#     start = 0
#     length = float('inf')
#     #用于记录最终的结果
#
#     #对window和need进行初始化
#     for s in T:
#         if s not in need.keys():
#             need[s] = 1
#         else:
#             need[s] += 1
#     for s in T:
#         if s not in window.keys():
#             window[s] = 0
#     while right < len(S):
#         char = S[right]
#         right += 1
#         if char in need.keys():
#             window[char] += 1
#             if window[char] == need[char]:
#                 valid += 1
#         while valid == len(need.keys()):
#             #开始缩减左侧：
#             if (right-left) < length:
#                 start = left
#                 length = right-left+1
#             d = S[left]
#             left += 1
#             if d in need.keys():
#                 if window[d] == need[d]:
#                     valid -= 1
#                 window[d] -= 1
#
#     print(start,length)
#     return S[start:length+1] if length != float('inf') else ""
#
# # print(slidwindow(S,T))
#
def checkInclusion(S,T):
    window = {}
    need = {}
    left = 0
    right = 0
    valid = 0 #用于指示是否该缩减窗口了，当valid == len(need)

    #用于记录最终的结果

    #对window和need进行初始化
    for s in T:
        if s not in need.keys():
            need[s] = 1
        else:
            need[s] += 1
    for s in T:
        if s not in window.keys():
            window[s] = 0

    while right < len(S):
        char = S[right]
        right += 1
        if char in need.keys():
            window[char] += 1
            if window[char] == need[char]:
                valid += 1
        #什么时候开始缩？
        while (right-left) >= len(T):
            #开始缩减左侧：
            if valid == len(need):
                return (left,right)
            d = S[left]
            left += 1
            if d in need.keys():
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return False

print(checkInclusion(S,T))
#
# if checkInclusion(S,T):
#     print("TRUE")
# else:
#     print("FALSE")

# string = "55"
# print(string.isdigit())