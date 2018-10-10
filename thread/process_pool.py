import multiprocessing as mp
from time import sleep
import os

def work(msg):
    sleep(2)
    print(msg)
    return "work return" + msg


pool = mp.Pool(processes = 4)

result = []
for i in range(10):
    msg = "hello %d"%i
    r = pool.apply_async(work,(msg,))
#    pool.apply(work,(msg,))
    result.append(r)

pool.close()

for r in result:
    print(r.get())

pool.join()
