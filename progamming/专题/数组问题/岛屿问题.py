grid = [[0,0,1,0,0,0],[0,0,0,0,0,1],[1,0,0,0,0,0]]
def dfs(grid,cur_i,cur_j):
    """
    定义函数功能：以当前cur_i,cur_j为坐标的联通区域的大小
    :param grid:
    :param cur_i:
    :param cur_j:
    :return:
    """
    if cur_i < 0 or cur_j < 0 or cur_i== len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
        return 0
    grid[cur_i][cur_j] = 0#关键一步，遍历完这一个点以后即将其置为0，(从递归角度看就是缩减子问题规模)
    ans = 1
    for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
        next_i,next_j = cur_i+i,cur_j+j
        ans += dfs(grid,next_i,next_j)
    return ans

def maxAreaIsland(grid):
    num = 0
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            ans = 0
            ans = max(dfs(grid,i,j),ans)
            if ans > 0:
                num += 1
    return num
print(maxAreaIsland(grid))