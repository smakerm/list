# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#斐波那契数列：
#递归：有一个函数，它自己调用自己；
#Fab(n) = Fab(n-1)+Fab(n-2)   n >= 2
#         1                   0<= n < 2
#				                    n是自然数；
def Fab(n):
    # 0 <= n 并且 n belongs to N
    # a 并且 b <==> ~a 或者 ~b  
    if type(n) != type(1):
        print("非法输入")
        return None
    if n < 0:
        print("非法输入")
        return None        
    if n < 2:
        return 1
    else:
        return Fab(n-1)+Fab(n-2)
    
#for i in range(0,10):
#    print(Fab(i))
#print(Fab(-1))
#print(Fab(1.5))
print(Fab(1000))
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
        
