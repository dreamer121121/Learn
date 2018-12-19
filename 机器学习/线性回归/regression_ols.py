from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def loadDataset(filename):
    f = open(filename,'r')
    dataset = []
    labelset = []
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split('\t')
        dataset.append(float(line[1]))
        labelset.append(float(line[-1]))
    return dataset,labelset

def ols_gradient(X,Y):#梯度下降实现最小二乘法  （一元线性回归）
    n = X.shape[0]
    X = X.tolist()  #变量X
    Y = Y.tolist()
    lr = 0.001
    w = [0,0]
    min_loss = 0.0000001
    pre_w = [float('inf'),float('inf')]
    while True:
        # 求解w0
        for i in range(n):
            temp0 = 0
            temp0 += w[0]+w[1]*X[i]-Y[i]
        # 求解w1
        for i in range(n):
            temp1 = 0
            temp1 += (w[0]+w[1]*X[i]-Y[i])*X[i]

        # 更新参数w值(同步更新）
        w[0] -=lr*temp0
        w[1] -=lr*temp1

        if abs(w[0]-pre_w[0]) < min_loss and abs(w[1]-pre_w[1]) < min_loss:
            break
        else:
            pre_w[0] = w[0]
            pre_w[1] = w[1]
    return w

def fig(X,Y,w):
    Y1 = w[0]+1 + w[1]*X
    plt.plot(X,Y1)
    plt.scatter(X,Y,c='r')
    plt.xlim(0,1)
    plt.ylim(2,5)
    plt.xticks(np.arange(0,1.1,0.1))
    plt.yticks(())
    plt.show()

if __name__ == '__main__':
    X,Y = loadDataset('ex0.txt')
    X = np.array(X)
    Y = np.array(Y)
    print(X)
    print(Y)
    w = ols_gradient(X,Y)
    print("学习得到的最优w值：",w)
    fig(X,Y,w)

