# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#交叉验证法寻找最优KNN的K值
import os
import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import cross_val_score
#处理数据
os.chdir(r'C:\Users\jack xia\Desktop\sklearn学习\数据集dataset\breast_cancer_datasets')
train_data=pd.read_csv('train_datasets.csv')
test_data=pd.read_csv('test_datasets.csv')
train_x=train_data.iloc[:,1:31]#以索引方式数字索引dataframe
train_y=train_data.iloc[:,31]
test_x=test_data.iloc[:,1:31]
test_y=test_data.iloc[:,31]
k_scores={}
for k in range(1,270):
    #构建分类器
    knn=neighbors.KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn,train_x,train_y,cv=10,n_jobs=1)
    k_scores[k]=scores.mean()
best_k=1
for key in k_scores:
    if k_scores[best_k]<=k_scores[key]:
        best_k=key
    else:
        continue
print (str(best_k)+':'+str(k_scores[best_k]))

        

    
    
    










        









