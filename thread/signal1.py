from signal import *
import os,time

def handler(sig, frame):
    if sig == SIGALRM:
        print("收到了时钟信号")
    if sig == SIGINT:
        print("收到了就是不暂停")


alarm(7)

signal(SIGALRM, handler)
signal(SIGINT, handler)

while True:
    print("waiting signal")
    time.sleep(1)
