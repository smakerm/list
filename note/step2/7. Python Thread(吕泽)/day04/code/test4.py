from test import *
import multiprocessing 
import time 

counts = []

t = time.time() 
for x in range(10):
    th = multiprocessing.Process\
    (target = count,args = (1,1))
    th.start()
    counts.append(th)

n = len(counts)
while True:
    for th in counts:
        if not th.is_alive():
            n -= 1
    if n <= 0:
        break 
print("Process cpu",time.time()-t)

