# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:37:54 2018

@author: outao
"""
import os
from sklearn import tree
from sklearn import datasets
import graphviz
# os.chdir(r'C:\Users\jack xia\Desktop\连接公司\ARGUS\机器学习\决策树')
# 整理数据
data = datasets.load_iris()
train_X = data['data']
train_y = data['target']
clf = tree.DecisionTreeClassifier()  # 构建分类器
clf = clf.fit(train_X, train_y)
dot_data = tree.export_graphviz(clf, out_file=None)
# graph=graphviz.Source(dot_data)
# graph.render('iris')
# result=clf.predict(train_X[:1,:])
