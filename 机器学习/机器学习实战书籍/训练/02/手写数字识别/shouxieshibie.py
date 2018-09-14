# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:41:44 2018

@author: outao
"""
import os
import re 
import numpy as np
import pandas as pd
from sklearn import neighbors
path1=r'C:\Users\outao\Desktop\work\机器学习\机器学习实战书籍\Ch02\trainingDigits'
path2=r'C:\Users\outao\Desktop\work\机器学习\机器学习实战书籍\Ch02\testDigits'

def preprocess(Files):
    data=[]
    for file in Files:
        temp=p_one_file(file)
        data.append(temp)
    data=np.array(data)
    return data

       
def p_one_file(file):#处理一个文件
    f=open(file,'r')
    content=f.readlines()
    c2list=[]
    for i in range(32):
        for j in range(32):
            c2list.append(content[i][j])
    #添加标签
    z='(\w)_*'#获取标签
    label=re.search(z,file).group(1)
    c2list.append(label)
    return c2list

def KNN(trian,test):
    train_X=train[:,0:1024]
    train_y=train[:,1024]
    test_X=test[:,0:1024]
    test_y=test[:,1024]
    sample=test_X[945,:]
    sample=sample.reshape(1,1024)
    knn=neighbors.KNeighborsClassifier(n_neighbors=300)
    knn.fit(train_X,train_y)
    result=knn.predict(sample)
    print(result)
    #print("预测结果为：----------------------")
    #print(result)

if __name__=='__main__':
    os.chdir(path1)
    Files1=os.listdir(path1)
    train=preprocess(Files1)
    os.chdir(path2)
    Files2=os.listdir(path2)
    test=preprocess(Files2)
    KNN(train,test)