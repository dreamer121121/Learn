from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields注意减去1
    # print(numFeat)
    dataMat = []; labelMat = []  #label矩阵
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T #转换为矩阵
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print ("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

if __name__ == '__main__':
    xArry,yArr = loadDataSet('ex0.txt')
    w = standRegres(xArry,yArr)
    print("学习所得w向量",w)


