# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:11:48 2018

@author: jack xia
"""
import numpy
from numpy import linalg as la
import pandas as pd
test=numpy.random.poisson(lam=2, size=5000).reshape(100,50)
test=pd.DataFrame(test)
#test.to_csv('ingmaital.csv')
U,sigma,V=la.svd(test)
#----------------------------------------------
print(type(sigma))
sigma=sigma.tolist()
sum=0
k=0
total_sum=0
print(len(sigma))
for s in sigma:
    total_sum+=s*s
for s in sigma:
    sum+=s*s
    k+=1
    if sum > (total_sum*0.9):
        break
print("k=%d"%k)   
    