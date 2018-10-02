# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:21:35 2018

@author: outao
"""
import skimage.io as io
import numpy as np
from sklearn.decomposition import PCA
import math
import random
from PIL import Image
import pylab as pl


def loadData(number):
    if number == 1:
        path = r'C:/Users/outao/Desktop/work/机器学习/PCA/人脸数据集/yale_faces/*.bmp'
        num = 11
    if number == 2:
        path = r'C:/Users/outao/Desktop/github机器学习库/Machine-Learning/pic/SFA/orl_faces_full/*.pgm'
        num = 10
    pictures = io.ImageCollection(path)  # 以列表形式返回一个图片文件集
    data = []
    for i in range(len(pictures)):
        data.append(
            np.ravel(pictures[i].reshape(1, pictures[i].shape[0] * pictures[i].shape[1])))  # data是一个列表其中的元素为ndarray数组
    label = []
    for i in range(len(data)):  # 总共165张图片
        label.append(int(i / num))  # 给每张图片添加标签
    return np.matrix(data), np.matrix(label).T  # 把ndarray数组转换成矩阵并返回


def SplitData(data, label, number, propotion):
    if number == 1:
        classes = 15
    elif number == 2:
        classes = 40
    samples = data.shape[0]
    perClass = int(samples / classes)
    selected = int(perClass * propotion)

    trainData, testData = [], []
    trainLabel, testLabel = [], []
    count1 = []
    # 找出训练样本
    for i in range(classes):  # 控制第几个人
        count2 = []  # count主要用来去重，避免重复选一个样本
        for j in range(selected):  # 控制要选的训练样本的数量
            k = random.randint(0, perClass-1)
            while k in count2:
                k = random.randint(0, perClass - 1)
            trainData.append(np.ravel(data[perClass*i+k]))
            trainLabel.append(np.ravel(label[perClass*i+k]))
            count2.append(k)
            count1.append(perClass*i+k)
    # 找出测试样本
    for i in range(samples):
        if i not in count1:
            testData.append(np.ravel(data[i]))
            testLabel.append(np.ravel(label[i]))

    return np.matrix(trainData), np.matrix(trainLabel), np.matrix(testData), np.matrix(testLabel)


def Faceidentifier(trainDatas, trainLabel, testDatas, testLabel):
    pass


def reconstruct(Datas,data):
    T = data * Datas
    for i in range(1,30):
        img = T[:,i].reshape(100,100)
        new_im = Image.fromarray(img)
        new_im.show()

if __name__ == '__main__':
    data, label = loadData(1)
    data = data.astype(np.float64)
    #print(data)
    trainData, trainLabel, testData, testLabel = SplitData(data, label, 1, 0.6)
    pca =PCA(30, True, True)
    trainDatas = pca.fit_transform(trainData)
    testDatas = pca.transform(testData)
    print(pca.components_.T.shape)#直接调用pca.components_获取主成分（即特征向量）
    Datas = pca.components_.reshape((30, 100, 100))  # 降维后的矩阵
    img = Datas[0].reshape((100, 100))
    print(img.shape)
    new_im = Image.fromarray(img)
    new_im.show()
    r'''
    for i in range(data.shape[1]):
        sum = 0
        mean = 0
        for j in range(data.shape[0]):
            sum += data[j, i]
        mean = sum/data.shape[0]
        li = data[:, i] - mean
        for k in range(data.shape[0]):
            data[k, i] = li[k, 0]
    '''
    #print(data)
    #new_data = np.linalg.pinv(data)  # 求原data的逆矩阵
    #reconstruct(Datas, new_data)
    # new_im.save('learn.bmp')
    # 进行分类
    # Faceidentifier(trainDatas, trainLabel, testDatas, testLabel)
