# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:57:02 2018

@author: Administrator
"""

from multiprocessing import Process
g_num = 100
import time

def getTime(interval):
    global g_num
    while True:
        g_num += 100
        print("in child process g_num is %d"%g_num)

if __name__ == "__main__":
    p = Process(target=getTime,args=(1,))
    p.start()
    
    while True:
        time.sleep(2)
        g_num += 1
        print("in p process g_num is %d"%g_num)
    
    
    