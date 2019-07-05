from numpy import *
# from math import * #尚不明白为何引入math库会引发错误

# def load_dataset():
#     # datamat = [];labelmat = []
#     # with open ("testSet.txt",'r') as f:
#     #     content = f.readlines()
#     # for line in content:
#     #     instance = line.strip().split()
#     #     datamat.append([1.0,float(instance[0]),float(instance[1])])
#     #     labelmat.append(int(instance[2]))
#     # return datamat,labelmat
#     dataMat = []; labelMat = []
#     fr = open('testSet.txt')
#     for line in fr.readlines():
#         lineArr = line.strip().split()
#         dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
#         labelMat.append(int(lineArr[2]))
#     return dataMat,labelMat
#
#
# def sigmoid(inX):
#     print("--inx--",type(inX))
#     return 1.0/(1+exp(-inX))
#
# def gradAscent(dataMatIn,classLabels):
#     # dataMatrix = mat(dataMatIn)
#     # labelMat = mat(classLables).transpose()#转置矩阵
#     # m,n = shape(dataMatrix)
#     # alpha = 0.001  #学习速率
#     # maxCycles = 500 #迭代次数
#     # weights = ones((n,1))#初始化权重矩阵
#     # #开始迭代上升
#     # for i in range(maxCycles):
#     #     h = sigmoid(dataMatrix * weights)
#     #     error = labelMat - h
#     #     weights += alpha * (dataMatrix * error)
#     # return weights
#     dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
#     labelMat = mat(classLabels).transpose() #convert to NumPy matrix
#     m,n = shape(dataMatrix)
#     alpha = 0.001
#     maxCycles = 500
#     weights = ones((n,1))
#     for k in range(maxCycles):              #heavy on matrix operations
#         print("第"+str(k)+"次迭代")
#         h = sigmoid(dataMatrix*weights)     #matrix mult
#         error = (labelMat - h)              #vector subtraction
#         weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
#     return weights



def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     #matrix mult
        error = (labelMat - h)              #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
    return weights


def plotBestFit():
    import matplotlib.pyplot as plt
    dataMat,labelMat = loadDataSet()
    dataArr = array(dataMat)
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


dataArr,labelMat = loadDataSet()
print(gradAscent(dataArr,labelMat))
plotBestFit()