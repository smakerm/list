import multiprocessing as mp
from socket import *
import os
import time


def showdir(c):
    c.send(b"ls")

def download(c):
    c.send(b"downloading...")

def upload(c):
    c.send(b"uploading...")

def handler(c):
    while True:
        data = c.recv(1024).decode()
        if data == 'ls':
            showdir(c)
        elif data == 'wget':
            download(c)
        elif data == 'wput':
            upload(c)
        elif data == 'quit':
            c.close()
            break
        else:
            c.send(b"input error")


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
#s.setsocketopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        os._exit
    except Exception:
        continue
    print("connect from %s at %s" %(c.getpeername(), time.ctime()))

    p = mp.Process(target=handler, args=(c,))
#    p = Process(target=handler,args=(c,))
#    p = Process(target=handler, args=(c,))
    p.Daemon = True
    p.start()
    







