import multiprocessing as mp 
import os
import time 

def th1():
    print(os.getppid(),"----",os.getpid())
    print('吃饭早饭')
    time.sleep(1)
    print('吃饭午饭')
    time.sleep(6)
    print('吃饭晚饭')
    time.sleep(3)

def th2():
    print(os.getppid(),"----",os.getpid())
    print("睡午觉")
    time.sleep(3)
    print("睡觉")
    time.sleep(3)

def th3():
    print(os.getppid(),"----",os.getpid())
    print("打豆豆")
    time.sleep(5)
    print("打豆豆")
    time.sleep(2)

things = [th1,th2,th3]
process = []

for th in things:
    p = mp.Process(target = th)
    process.append(p)

for p in process:
    p.start()

for i in process:
    i.join(1)

print("++++++++++++++++++")

