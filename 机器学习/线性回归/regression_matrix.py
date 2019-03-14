from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields注意减去1
    dataArr = []; labelArr = []  #label矩阵
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataArr.append(lineArr)
        labelArr.append(float(curLine[-1]))
    return dataArr,labelArr

def standRegres(xArr,yArr):
    xMat = mat(xArr);yMat = mat(yArr).T #转换为矩阵
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print ("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

def predict(xArry,yArry,w):
    xMat = np.mat(xArry);yMat = np.mat(yArry)
    wMat = np.mat(w)
    #绘制原始数据图像
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print("---type(xMat[:,1].flatten())---",type(xMat[:,1].flatten().A[0]))
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    #flatten()降维函数，默认按行降维，返回的是一个一维矩阵
    #matrix.A返回的是Array对象。
    plt.show()

    # yHat = xMat*wMat #计算预测值


if __name__ == '__main__':
    xArry,yArr = loadDataSet('ex0.txt')
    w = standRegres(xArry,yArr)
    predict(xArry,yArr,w)


