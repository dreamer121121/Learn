# 构建一张图
graph = dict()
graph['1'] = ['2', '3']
graph['2'] = ['4', '5']
graph['3'] = ['6', '7']
graph['4'] = []
graph['5'] = []
graph['6'] = []
graph['7'] = []
searchd_node = []


def dfsvisit(u):
    for v in graph[u]:
        if v not in searchd_node:
            searchd_node.append(v)
            dfsvisit(v)



def dfs(graph):
    for u in graph.keys():
        if u not in searchd_node:
            searchd_node.append(u)
            dfsvisit(u)



if __name__ == '__main__':
    dfs(graph)
    print(searchd_node)