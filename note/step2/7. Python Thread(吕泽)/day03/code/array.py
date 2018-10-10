from multiprocessing import Process,Array 
import time 
import ctypes

def fun(shm):
    for i in shm:
        print(i)
    # shm[0] = 'A'

# shm = Array('i',[1,2,3,4,5])
shm = Array(ctypes.c_char,6)

p = Process(target = fun,args = (shm,))
p.start()
p.join()

for i in shm:
    print(i)
