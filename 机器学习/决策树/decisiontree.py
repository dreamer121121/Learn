# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:37:54 2018

@author: outao
"""
import os
from sklearn import tree
from sklearn import datasets
os.chdir(r'C:\Users\outao\Desktop\work\机器学习\决策树')
#整理数据
data=datasets.load_iris()
train_X=data['data']
train_y=data['target']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(train_X,train_y)
dot_data=tree.export_graphviz(clf,out_file=None)

#result=clf.predict(train_X[:1,:])

