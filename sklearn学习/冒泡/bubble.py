# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
a=[5,7,8,2,15,4]  
r'''
for i in range(len(a)-1):#控制循环次数
    l=np.arange(i,len(a)-1).tolist()
    l.sort(reverse=True)
    for j in l:#控制每一次要比较的次数
        if a[j]<a[j+1]:
            temp=a[j]s
            a[j]=a[j+1]
            a[j+1]=temp
        else:
            continue
print(a)
'''
r'''
i=1
while i<=len(a)-1:
    for j in range(len(a)-i):
        print (j)
        if a[j]>a[j+1]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
        else:
            continue
    i+=1
print (a)
'''
       
        

 

























