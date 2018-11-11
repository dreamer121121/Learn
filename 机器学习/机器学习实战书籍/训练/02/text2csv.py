# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:24:29 2018

@author: outao
"""
import os
import numpy as np
import pandas as pd
os.chdir(r'C:\Users\outao\Desktop')
f=open('datingTestSet.txt','r')
text=f.readlines()
data=[]
for eachline in text:
    eachline=eachline.strip('\n').split('\t')
    data.append(eachline)
data=np.array(data)
data=pd.DataFrame(data,columns=['飞行常客里程数','玩游戏视频所占','每周消费的冰淇淋数','类型'])
data.to_csv('dataSet.csv')

