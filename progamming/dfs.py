# 构建一张图
graph = dict()
graph['1'] = ['2', '3']
graph['2'] = ['4', '5']
graph['3'] = ['6', '7']
graph['4'] = []
graph['5'] = []
graph['6'] = []
graph['7'] = []
searchd_node = []  # 记录遍历节点的顺序


def dfsvisit(u):
    if graph[u]:  # 判断u节点是否有子节点
        for v in graph[u]:
            if v not in searchd_node:
                searchd_node.append(v)
                dfsvisit(v)
            else:
                continue
    else:
        pass


def dfs(graph):
    for u in graph.keys():  # 从节点1开始便利图片
        if u not in searchd_node:
            searchd_node.append(u)
            dfsvisit(u)
        else:
            continue


if __name__ == '__main__':
    dfs(graph)
    print(searchd_node)
