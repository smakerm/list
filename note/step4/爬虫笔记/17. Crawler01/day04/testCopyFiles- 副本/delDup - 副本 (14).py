# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:24:40 2018

@author: Administrator
"""
#从一个list中去除重复的元素
# 返回list
def DelDupli(L):
    return list(set(L)) # [1, 34, 3, 4, 2, 8, 54]

def DelDupli2(L):
    lst = []            # 空间复杂度会增加
    for x in L:
        if x not in lst:
            lst.append(x)
    return lst          # [1, 3, 4, 34, 54, 2, 8]

def DelDupli3(L):
    myDict = {}
    for i in L:
        myDict[i] = 0
    L = list(myDict.keys())
    return L

L = [1,3,3,3,4,3,34,3,54,3,4,2,8]
print(DelDupli(L)) # 1,3,4,34,54,2,8
print(DelDupli2(L))
print(DelDupli3(L)) #[1, 3, 4, 34, 54, 2, 8]
