# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:05:17 2018

@author: Administrator
"""
#组合数：
#	从n个不同元素中，任取m(m≤n)个元素并成
#一组，叫做从n个不同元素中取出m个元素的一个组合
#；从n个不同元素中取出m(m≤n)个元素的所有组合的
#个数，叫做从n个不同元素中取出m个元素的组合数。

#C(n,m) = n!/(m!(n-m)!)
#n! = 1*2*3*...*n
#n! = n*(n-1)!
#def F(n):
#   if n == 1:
#     return 1 
#   return n*F(n-1)
#
#C(n,0)=1，C(n,n)=1
#C(n,m)=C(n,n-m)
#C(n,m)=C(n-1,m-1)+C(n-1,m)
# n >= m

# C(3,2)=C(3,1)=3
# A,B,C

def ComNum(n,m):
    """
    用递归方法来计算 C(n,m) = n!/(m!(n-m)!)
    """
    #C(n,0)=C(n,n)=1
    if m==0 or m==n:
        return 1
    
    return ComNum(n-1,m-1)+ComNum(n-1,m) 

n,m = 6,4 # 6*5/2 = 15
print(ComNum(n,m))










