# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:33:10 2018

@author: Administrator
"""
# queue
# deque
import collections
#import threading
import multiprocessing
import time

candle = collections.deque("candle")

def burn(direction, nextSource):
    print("burning")
    while True:
        try:
            next = nextSource()
            time.sleep(0.1)
        except IndexError:
            break
        else:
            print('%s : %s\n'%(direction, next))
    print("Done %s \n"%direction)
    
# 创建两个线程，分别从两端去双向队列中取值
#观察有没有异常情况
#left = threading.Thread(target=burn, 
#                        args=('left', candle.popleft))
#right = threading.Thread(target=burn, 
#                         args=('right', candle.pop))

left = multiprocessing.Process(target=burn, args=('left', candle.popleft))
right = multiprocessing.Process(target=burn, args=('right', candle.pop))

left.start()
right.start()

left.join()
right.join()
    

 