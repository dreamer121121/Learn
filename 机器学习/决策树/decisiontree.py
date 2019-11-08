# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:37:54 2018

@author: outao
"""
#Sklearn实现
# import os
# from sklearn import tree
# from sklearn import datasets
# import graphviz
# # os.chdir(r'C:\Users\jack xia\Desktop\连接公司\ARGUS\机器学习\决策树')
# # 整理数据
# data = datasets.load_iris()
# train_X = data['data']
# train_y = data['target']
# clf = tree.DecisionTreeClassifier()  # 构建分类器
# clf = clf.fit(train_X, train_y)
# dot_data = tree.export_graphviz(clf, out_file=None)
# # graph=graphviz.Source(dot_data)
# # graph.render('iris')
# # result=clf.predict(train_X[:1,:])


from math import log


def create_dataset():
    data_set = [[1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']]
    labels = ['no surfacing','flippers']
    return data_set,labels

def calcShannonEnt(dataset):

    """用于计算输入数据集的香农熵"""
    numEntries = len(dataset)
    labelCounts = {}
    for entry in dataset:
        label = entry[-1]
        if label not in labelCounts.keys():labelCounts[label] = 0
        labelCounts[label] += 1
    shannonEnt = 0.0
    for key in labelCounts.keys():
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

dataset,lables = create_dataset()

def splitDataset(dataset,axis,value):
    retDataset = []
    for entry in dataset:
        if entry[axis] == value:
            temp = entry[:axis]
            temp += entry[axis+1:]
            retDataset.append(temp)
    return retDataset


def chooseBestFeaturestosplit(dataset):
    """
    计算按每一个特征进行数据集划分后的信息增益
    :param dataset:
    :return:
    """
    numFeatures = len(dataset[0])-1
    baseEntroy = calcShannonEnt(dataset)
    bestInfogain = 0.0;bestFeature = -1
    for i in range(numFeatures):
        Featlist = [example[i] for example in dataset]
        uniquevals = set(Featlist)
        newEntroy = 0.0
        for val in uniquevals:
            subdataset = splitDataset(dataset,i,val) #划分数据集
            prob = float(len(subdataset))/float(len(dataset))
            newEntroy += prob * calcShannonEnt(subdataset)
        gaininfo = baseEntroy-newEntroy #计算按第i个特征划分数据集的信息增益
        if gaininfo > bestInfogain:
            bestInfogain = gaininfo
            bestFeature = i
    return bestFeature

def  majorityCnt(classList):
    """
    叶子节点分属不同类别时采用多数投票原则
    :param classList:
    :return:
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] += 1
    sortedClasscount = sorted(classCount.items(),key = lambda item:item[1],reverse=True)
    return sortedClasscount[0][0]

def createTree(dataset,labels):
    """
    递归法创建决策树
    :param dataset:
    :param labels:
    :return:
    """

    classList = [example[-1] for example in dataset ] #列表解析式。

    #两个递归的终止条件
    #终止条件1：当前节点数据集中所有数据的分类相同
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    #终止条件2：数据集中所有属性都已被遍历完但同一叶子节点中的数据分类还是不相同
    #此时需要采用多数投票原则
    if len(dataset[0]) ==  1:
        return majorityCnt(classList)

    bestFeatIndex = chooseBestFeaturestosplit(dataset)
    bestFeatLabel = labels[bestFeatIndex]
    mytree = {bestFeatLabel:{}}
    del(labels[bestFeatIndex])
    Featevals = [example[bestFeatIndex] for example in dataset]
    uniquevals = set(Featevals)
    for val in uniquevals:
        subdataset = splitDataset(dataset,axis=bestFeatIndex,value=val)
        sublabels = labels[:]
        mytree[bestFeatLabel][val] = createTree(subdataset,sublabels)
    return mytree


#绘制决策树
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(myTree, parentPt, nodeTxt):#if the first key tells you what feat was split on
    numLeafs = getNumLeafs(myTree)  #this determines the x width of this tree
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]     #the text label for this node should be this
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':#test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key],cntrPt,str(key))        #recursion
        else:   #it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD



def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
    #createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()


fr = open("lenses.txt",'r')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lenseslabels = ['age','prescript','astigmatic','tearRate']
lensesTree = createTree(lenses,lenseslabels)
# createPlot(lensesTree)















