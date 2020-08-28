#0-1背包问题
# costs = [3,2,3,4,6]
# values = [5,6,7,1,10]#表示价值
# V = 8
# dp = [[0]*(V+1) for i in range(len(costs)+1)] #初始化一个二维数组
#
# costs.insert(0,0)
# values.insert(0,0)
#
# # dp[i][j]表示：在前i个物品中进行选择，体积不超过j的情况下所取商品的最大价值
# for i in range(1,len(costs)):
#     for j in range(1,V+1):
#         if j < costs[i]: #注意此处用i表示第一个物品的体积
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-costs[i]]+values[i])
# print(dp)
""""
dp
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 5, 5, 5, 5, 5, 5]
[0, 0, 6, 6, 6, 11, 11, 11, 11]
[0, 0, 6, 7, 7, 13, 13, 13, 18]
[0, 0, 6, 7, 7, 13, 13, 13, 18]
[0, 0, 6, 7, 7, 13, 13, 13, 18]
"""

#优化空间复杂度，使用一维数组

# dp = [0]*(V+1)
# costs.insert(0,0)
# for i in range(1,len(costs)):
#     for j in range(V,0,-1):#当使用一维数组时明白为何一定要倒序进行数组填充
#         if j >= costs[i]: #要保证j要大于volumes[i-1]
#             dp[j] = max(dp[j],dp[j-costs[i]]+values[i])
# print(dp)


#完全背包问题

# dp = [[0]*(V+1) for _ in range(len(values)+1)]
# costs.insert(0,0)
# values.insert(0,0)
# for i in range(1,len(values)):
#     for j in range(1,V+1):
#         if costs[i] > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             for k in range(j//costs[i]+1):
#                 dp[i][j] = max(dp[i][j],dp[i-1][j-k*costs[i]]+k*values[i])
# print(dp)

import functools
def cmp(x1,x2):
    if int(str(x1)+str(x2)) < int(str(x2)+str(x1)):
        return True
    else:
        return False
a = [1,2,3]
a.sort(key=functools.cmp_to_key(cmp))