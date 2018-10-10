from socket import *
import threading
import os

def handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到",data)
        c.send(b"recrive your message")
    c.close()

#1. 创建套接字 绑定 监听
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

while True:
    try:
        c, addr = sockfd.accept()
    except KeyboardInterrupt:
        sockfd.close()
        os._exit(0)
    except Exception:
        continue
    print("connect seccess...",c.getpeername())
    
    t = threading.Thread(target=handler, args=(c,))
    t.setDaemon(True)
    t.start()


