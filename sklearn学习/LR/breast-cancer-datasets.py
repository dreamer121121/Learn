import os
from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np
path=r'C:\Users\jack xia\Desktop\sklearn学习'
os.chdir(path)
initial_data=load_breast_cancer()#数据类型为sklearn.utils.bounch
column=initial_data['feature_names']
#把ndaarray类型转换为dataframe类型
data=pd.DataFrame(initial_data['data'],index=range(569),columns=column)
data['classification']=initial_data['target']#dataframe类型存储数据
data.to_csv('breast-cancer.csv')
#从数据集中抽取样本作为训练样本和测试样本
data_train=data.loc[range(300),:]
data_train.to_csv('train_datasets.csv')
data_test=data.loc[300:,:]
data_test.index=range(269)
data_test.to_csv('test_datasets.csv')
