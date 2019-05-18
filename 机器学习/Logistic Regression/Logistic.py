from numpy import *
from math import *
import numpy as np

def load_dataset():
    datamat = [];labelmat = []
    with open ("testSet.txt",'r') as f:
        content = f.readlines()
    for line in content:
        instance = line.strip().split()
        datamat.append([1,instance[0],instance[1]])
        labelmat.append(int(instance[2]))
    return datamat,labelmat

def sigmoid(inx):
    return 1.0/(1+exp(-inx.tolist()))

def gradAscent(dataMatIn,classLables):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLables).transpose() #转置矩阵
    m,n = shape(dataMatrix)
    alpha = 0.1  #学习速率
    maxCycles = 500 #迭代次数
    weights = ones((n,1),np.float32)#初始化权重矩阵
    #开始迭代上升
    for i in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = labelMat - h
        weights += alpha * (dataMatrix.T * error)
    return weights

def plotBestFit():
    import matplotlib.pyplot as plt
    # weights = wei.getA() #将矩阵转换为数组Array
    dataMat,labelMat = load_dataset()
    dataArr = array(dataMat)
    print("--dataArr--")
    n = shape(dataArr)[0]
    xcord1 = [];ycord1 = []
    xcord2 = [];ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    plt.show()


# plotBestFit()

dataArr,labelMat = load_dataset()
print(gradAscent(dataArr,labelMat))
