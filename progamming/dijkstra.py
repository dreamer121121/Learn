# 初始化图参数
G = {1: {1: 0, 2: 1, 3: 12},
     2: {2: 0, 3: 9, 4: 3},
     3: {3: 0, 5: 5},
     4: {3: 4, 4: 0, 5: 13, 6: 15},
     5: {5: 0, 6: 4},
     6: {6: 0}}

searchd_node = []

def dijkstra(G):
     # 初始化
     priority_queue = dict((k, float("inf")) for k in G.keys())
     s = '1'
     t = '6'
     priority_queue[s] = 0
     while priority_queue:
          # 进行extra_min操作
          min = float("inf")
          for v in priority_queue.keys():
               if priority_queue[v] < min:
                    min = priority_queue[v]
                    u = v
          priority_queue.popitem(u)
          searchd_node.append(u)
          # -------------------------
          for v in u:
               # 更新priority_que






if __name__ == '__main__':
     dijkstra(G)
