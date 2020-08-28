#DP问题三要素：重叠子问题，最优子结构，状态转移方程
import datetime

def minEditdistance(s1,s2):
    len1 = len(s1)-1
    len2 = len(s2)-1
    def dp(i,j):
        #函数定义：求解s1[0.....i],s2[.....j]的最小编辑距离
        if i == -1:return j + 1      #递归边界
        if j == -1:return i + 1
        if s1[i] == s2[j]:
            return dp(i-1,j-1)
        else:
            #三种操作：插入，删除，替换
            return min(dp(i,j-1)+1,#插入 #状态转移方程
                       dp(i-1,j)+1,#删除
                       dp(i-1,j-1)+1) #替换
    return dp(len1,len2)

# start = datetime.datetime.now()
# minEditdistance("rad","apple")
# end = datetime.datetime.now()
# print(end-start)

class Node:
    def __init__(self,val,choice):
        self.val = val
        self.choice = choice #0表示什么也不做，1表示插入，2表示删除，3表示替换

def miEditDistance(s1,s2):
    #生成一张Table
    s1 = " "+s1
    s2 = " "+s2
    len1 = len(s1)
    len2 = len(s2)
    dp = [[Node(0,0) for _ in range(len1)] for _ in range(len2)]
    for i in range(1,len1):
        dp[0][i].val = i
    for j in range(1,len2):
        dp[j][0].val = j
    for i in range(1,len2):
        for j in range(1,len1):
            if s1[j] == s2[i]:
                dp[i][j].val = dp[i-1][j-1].val
            else:
                dp[i][j].val = min(dp[i][j-1].val+1,dp[i-1][j].val+1,dp[i-1][j-1].val+1)
                if dp[i][j].val == dp[i][j-1].val+1:
                    dp[i][j].choice = 1#删除
                elif dp[i][j].val == dp[i-1][j].val+1:
                    dp[i][j].choice = 2#插入
                elif dp[i][j].val == dp[i-1][j-1].val+1:
                    dp[i][j].choice = 3 #替换
    # print(dp[len2-1][len1-1].val)
    # 打印出方案
    i = len2-1
    j = len1-1
    while i >0 and j >0:
        print((i,j))
        tmp = dp[i][j].choice
        print(tmp)
        if tmp == 0 or tmp == 3:
            i -= 1
            j -= 1
        elif tmp == 1:
            j -= 1
        elif tmp == 2:
            i = i-1

    print(dp[1][1].val)



# start = datetime.datetime.now()
miEditDistance("rad","apple")
# end = datetime.datetime.now()
# print(end-start)





