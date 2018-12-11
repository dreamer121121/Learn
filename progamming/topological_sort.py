from stack import Stack

# 构建一张图
graph = dict()
graph['1'] = ['2', '3']
graph['2'] = ['4', '5']
graph['3'] = ['6', '7']
graph['4'] = []
graph['5'] = []
graph['6'] = []
graph['7'] = []
searchd_node = Stack()  # 记录遍历节点的顺序


def dfsvisit(u):
    if u not in searchd_node.stack:
        for v in graph[u]:
            dfsvisit(v)
        searchd_node.push(u)  # 压栈注意压栈的时间必须在u节点的所有节点均被访问到后u节点才能压栈


def dfs(graph):
    for u in graph.keys():  # 从节点1开始便利图片
        dfsvisit(u)


if __name__ == '__main__':
    dfs(graph)
    print(searchd_node.stack)
