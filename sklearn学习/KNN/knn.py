# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:12:35 2018

@author: jack xia
"""
from sklearn import neighbors
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
path=r'C:\Users\jack xia\Desktop\sklearn学习\数据集dataset\breast_cancer_datasets'
os.chdir(path)
#处理数据
train_data=pd.read_csv('train_datasets.csv')
train_X=train_data.iloc[:,1:31]
train_y=train_data.iloc[:,31]
test_data=pd.read_csv('test_datasets.csv')
test_X=test_data.iloc[0:,1:31]
test_y=test_data.iloc[0:,31]   
evaluate={}
for k in range(1,301):
    #构建迭代器
    knn=neighbors.KNeighborsClassifier(n_neighbors=k)
    #模型训练
    knn.fit(train_X,train_y)
    #模型预测
    result=knn.predict(test_X)
    #模型评价
    score=knn.score(test_X,test_y)
    evaluate[k]=score
#找到使得预测结果正确率最高的模型中n_neighbors的值
best_k=1
for k in evaluate.keys():
    if evaluate[best_k]<=evaluate[k]:
        best_k=k
    else:
        continue
#绘制图像
x=evaluate.keys()
y=evaluate.values()
#plt.xlabel('k')
#plt.ylabel('accuracy')
#plt.plot(x,y)
plt.title('dsgfds')
plt.savefig('knn.jpg')
plt.show()
#print ("使得模型预测结果最优的k值为：%d"%best_k)
#print ("模型的最高预测正确率为：%f"%evaluate[best_k])

    










