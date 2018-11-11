# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:47:00 2018

@author: outao
"""
def maxsubsum(a,left,right):
    if left == right:
        return a[left]
    center=(left+right)//2
    maxleftsum=maxsubsum(a,left,center)
    maxrightsum=maxsubsum(a,center+1,right)#递归调用
    
    #求包含左侧边界的最大值
    maxleftbordersum=0
    leftbordersum=0
    for i in range(center,left-1,-1):
        leftbordersum+=a[i]
        if leftbordersum > maxleftbordersum:
            maxleftbordersum = leftbordersum
            
    #求包含右侧边界的最大值
    maxrightbordersum=0
    rightbordersum=0
    for j in range(center+1,right+1):
        rightbordersum+=a[j]
        if rightbordersum > maxrightbordersum:
            maxrightbordersum = rightbordersum
            
     #比较三个值的大小返回最大值
    maxacrosssum = maxleftbordersum + maxrightbordersum
     
    r = max(maxleftsum,maxrightsum,maxacrosssum)
     
    return r
a = [1,-9,6,7,-2,5,6,-3]
print(maxsubsum(a,0,len(a)-1))
     
            
    
    
    
