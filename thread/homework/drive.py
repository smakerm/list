from signal import *
from multiprocessing import Process
import os


def saler_handler(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid,SIGUSR1)

def diver_handler(sig, frame):
    if sig ==


def saler():
    singal(SIGINT,saler_handler)
    

p = Process(name='maipiao', target=saler)
p.start()

signal(SIGUSR1,diver_handler)
