# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:06:18 2018

@author: Administrator
"""

#斐波那契数列：
#递归：有一个函数，它自己调用自己；
#Fab(n) = Fab(n-1)+Fab(n-2)   n >= 2
#         1                   0<= n < 2
#				                    n是自然数；

def Fab(n):
    """
    使用yield来返回值；用非递归来实现一个Fab(n)，使用yield来返回值；
    协程:是一个轻量级的线程
    """
    a, b, m = 0, 1, 0
    while m < n:
        yield b # b=1,a=1,m=1
        a, b, m = b, a + b, m + 1
        
        
t = Fab(20)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

