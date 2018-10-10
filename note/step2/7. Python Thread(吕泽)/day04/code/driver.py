from signal import * 
from multiprocessing import Process
import os
import time 

def saler_handler(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("python学完了，出去试试吧")
        os._exit(0)

def driver_handler(sig,frame):
    if sig == SIGUSR1:
        print("老司机带你学python")
    elif sig == SIGUSR2:
        print("python 知识多，积累最重要")
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)

def saler():
    signal(SIGINT,saler_handler)
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        time.sleep(2)
        print("开着python去远方")

p = Process(name = 'zhangjie',\
    target = saler)
p.start()

# 父进程处理信号部分
signal(SIGUSR1,driver_handler)
signal(SIGUSR2,driver_handler)
signal(SIGTSTP,driver_handler)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()