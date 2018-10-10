import multiprocessing as mp
from socket import *
import os


def handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到",data)
        c.send(b"recrive your message")
    c.close()


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

s = socket()
socket.setsocketopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

while True:
    try:
        print("wait connect......")
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        os._exit(0)
    except Exception:
        continue
    print("connect seccessful >> ", c.getpeername())

    p = mp.Process(target=handler, args=(c,))
    p.Daemon = True
    p.start()
