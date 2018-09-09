import os
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn import metrics
path=r'C:\Users\jack xia\Desktop\sklearn学习\数据集dataset\breast_cancer_datasets'
os.chdir(path)
#整理数据
train_data=pd.read_csv('train_datasets.csv').values
test_data=pd.read_csv('test_datasets.csv').values
train_x=train_data[:,1:31]
train_y=train_data[:,31].tolist()
test_x=test_data[:,1:31]
test_y=test_data[:,31]
#构建模型
lr=LogisticRegression()
#模型训练找到合适的theta
lr.fit(train_x,train_y)
#模型预测
result=lr.predict(test_x)
#模型评价
score=lr.score(train_x,train_y)
print (score)






