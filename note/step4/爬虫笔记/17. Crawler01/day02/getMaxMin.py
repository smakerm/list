# -*- coding: utf-8 -*-
"""
Created on Tue May 22 09:27:44 2018

@author: Administrator
"""
import math

# start+(end-start)/2  <--> (start+end)/2
def maxmin(L, start, end):
    """
    求出L的最大最小值的元组
    """
    if end-start <= 1:
        return (max(L[start],L[end]),min(L[start],L[end]))
    else:
        max1,min1 = maxmin(L, start, math.floor((start+end)/2))
        max2,min2 = maxmin(L, math.floor((start+end)/2)+1, end)
        return (max(max1,max2), min(min1,min2))

L=[1,2,6,7,-1,-5,9,8,13,21]
maxV,minV = maxmin(L, 0, len(L)-1)
print(maxV,minV)