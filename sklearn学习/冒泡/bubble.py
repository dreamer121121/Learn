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
def merge(a,b):
    temp=[]
    h=j=0
    while j <len(a) and h <len(b):
        if a[j]<b[h]:
            temp.append(a[j])
            j+=1
        else:
            temp.append(b[h])
            h+=1
    if j==len(a):
        for i in b[h:]:
            temp.append(i)
        
    if h==len(b):
        for i in a[j:]:
            temp.append(i)
    return temp



def merge_sort(sequence):
    if len(sequence)==1:
        return sequence
    middle=len(sequence)//2
    left=merge_sort(sequence[:middle])
    right=merge_sort(sequence[middle:])
    return merge(left,right)

if __name__=='__main__':
    result=merge_sort(a)
    print(result)

      
        

 

























