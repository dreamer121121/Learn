import json
import numpy as np
import pandas as pd
import os

f = open('paihang.txt', 'w')
# 读入数据
data = pd.read_csv('cluster_result.csv', encoding='gb18030').values
data = data.tolist()
print(data)
# # 计算城市得分
contribution1 = 76.246
contribution2 = 13.654
total_contribution = 89.9
w = [0, 0]
city_list = ['石家庄', '承德市', '张家口市', '秦皇岛市', '唐山市', '廊坊市', '保定市', '沧州市', '衡水市', '邢台市', '邯郸市']
for i in range(3):
    w[0] = contribution1 / total_contribution
    w[1] = contribution2 / total_contribution
scores = {}
i = 0
for city in city_list:
    score = data[i][1] * w[0] + data[i][2] * w[1]
    scores[city] = score
    i += 1
# 城市排行
print(type(scores.items()))  # dict.items()将原字典转换为可迭代对象
paihang = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(paihang)
f.write(json.dumps(paihang, ensure_ascii=False) + '\n')
f.write(json.dumps(w))
f.close()
