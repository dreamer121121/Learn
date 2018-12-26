import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import matplotlib

# 读取数据
data = pd.read_csv('julei.csv').values
print(data)
data = data.tolist()
X = []
Y = []
Z = []
label = []
for item in data:
    X.append(item[1])
    Y.append(item[2])
    Z.append(item[3])
    label.append(item[4])
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
print(label)

# 绘图
font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 10}
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig = plt.figure()
ax = Axes3D(fig)
for i in range(len(label)):
    if label[i] == 1:
        ax.scatter(X[i], Y[i], Z[i], color='red')
    elif label[i] == 2:
        ax.scatter(X[i], Y[i], Z[i], color='green')
    else:
        ax.scatter(X[i], Y[i], Z[i], color='blue')

ax.set_xlabel('财政状况和工业水平')
ax.set_ylabel('城市规模和农业发展水平')
ax.set_zlabel('居民收入水平')
ax.set_title('河北省各城市聚类分析结果')
plt.savefig('cluster.jpg')
plt.show()
