
from collections import deque
# 构建一张图
graph = dict()
graph['1'] = ['2', '3']
graph['2'] = ['4', '5']
graph['3'] = ['6', '7']
graph['4'] = []
graph['5'] = []
graph['6'] = []
graph['7'] = []

# 初始化
search_que = deque()  # 利用deque构建一个队列
searched_node = []
start_node = '1'
search_que.append(start_node)

def bfs(graph):
    while search_que:  # 当队列非空时
        u = search_que.popleft()  # 出队
        searched_node.append(u)
        V = graph[u]
        for each in V:
            if each not in searched_node:  # 判断该子节点是否已经被搜索过了
                search_que.append(each)  # 入队操作


if __name__ == '__main__':
    bfs(graph)
    print(searched_node)