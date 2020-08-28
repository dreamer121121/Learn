numbers = [31,-41,59,26,-53,58,97,-93,-23,84]
def FindGreatestSumOfSubArray(numbers): #函数定义返回连续子数组的最大和
    # if len(numbers) <= 1:
    #     return sum(numbers)
    # mid = len(numbers) >> 1
    # l = numbers[:mid]
    # r = numbers[mid:]
    # left_max = FindGreatestSumOfSubArray(l) #返回左边数组的连续子数组的最大值(相信他能实现)
    # right_max = FindGreatestSumOfSubArray(r) #返回右边数组的连续子数组的最大值（相信他能实现）
    # cross_max = cross_sum(l,r)
    # return max(left_max,right_max,cross_max)

    #方法二：使用动态规划，使用dp数组来存储包含当前num的最大连续子数组的和
    dp = [0]*len(numbers)
    dp[0] = numbers[0]
    i = 1
    while i < len(numbers):#dp[i]的含义是什么？
        dp[i] = max(dp[i-1]+numbers[i],numbers[i])#状态转移方程
        i += 1
    return max(dp)

def cross_sum(l,r):
    left_sum = 0
    max_left = float('-inf')
    for i in range(len(l)-1,-1,-1):
        left_sum += l[i]
        if left_sum > max_left:
            max_left = left_sum
    right_sum = 0
    max_right = float('-inf')
    for i in range(len(r)):
        right_sum += r[i]
        if right_sum > max_right:
            max_right = right_sum
    return max_left + max_right

print(FindGreatestSumOfSubArray(numbers))





