import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import matplotlib
import os
os.chdir(r'C:\Users\jack xia\Desktop\learn\learn\因子分析')

# 读取数据
data = pd.read_csv('4cluster_result.csv', encoding='gb18030').values
print(data)
data = data.tolist()
X = []
Y = []
label = []
for item in data:
    X.append(item[1])
    Y.append(item[2])
    label.append(item[3])
X = np.array(X)
Y = np.array(Y)
print(label)

# 绘图
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
for i in range(len(label)):
    if label[i] == 1:
        plt.scatter(X[i], Y[i], color='red')
    elif label[i] == 2:
        plt.scatter(X[i], Y[i], color='green')
    elif label[i] == 3:
        plt.scatter(X[i], Y[i], color='blue')
    else:
        plt.scatter(X[i], Y[i], color='black')

plt.xlabel('经济发展水平')
plt.ylabel('居民收入水平')
plt.title('河北省各城市聚类分析结果')
plt.savefig('cluster.jpg')
plt.show()
