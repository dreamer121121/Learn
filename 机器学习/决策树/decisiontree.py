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
# print(calcShannonEnt(dataset))

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
            newEntroy += prob * calcShannonEnt(dataset)
        gaininfo = newEntroy - baseEntroy #计算按第i个特征划分数据集的信息增益
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

def creatTree(dataset,labels):
    """
    递归法创建决策树
    :param dataset:
    :param labels:
    :return:
    """
    classList = [example[-1] for example in dataset ]

    #终止条件1：数据集中所有数据的分类相同
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
        mytree[bestFeatLabel][val] = creatTree(subdataset,sublabels)
    return mytree

















