# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:00:56 2018

@author: Administrator
"""
import numpy as np

def PrintSnakeMatrix(n):
#输入n(正整数), 如果n=4,输出:
#10 11 12 1      
#9  16 13 2      
#8  15 14 3      
#7  6  5  4    
    myArray = np.zeros((n,n), dtype=np.int16)
    
    num = 1
    i = 0     # i记录行
    j = n-1   # j记录列
    myArray[i][j] = num
    
    while num < n*n:
        while (i+1 < n and myArray[i+1][j] == 0):#向下,行不断增大，列不变
            i += 1
            num += 1
            myArray[i][j] = num
        while (j-1 >= 0 and myArray[i][j-1] == 0):#向左
            j -= 1
            num += 1
            myArray[i][j] = num
        while (i-1 >= 0 and myArray[i-1][j] == 0):#向上
            i -= 1
            num += 1
            myArray[i][j] = num
        while (j+1 < n and myArray[i][j+1] == 0): #向右
            j += 1
            num += 1
            myArray[i][j] = num
        
    print(myArray)

n =  int(input("请输入n的值:"))
PrintSnakeMatrix(n)