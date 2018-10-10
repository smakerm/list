from test import *
import threading 
import time 

def io():
    write()
    read()

counts = []

t = time.time() 
for x in range(10):
    th = threading.Thread(target = io)
    th.start()
    counts.append(th)

n = len(counts)
while True:
    for th in counts:
        if not th.is_alive():
            n -= 1
    if n <= 0:
        break 
print("Thread IO",time.time()-t)
