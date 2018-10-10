from socket import *
import os
import signal


def handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到",data)
        c.send(b"recrive your message")
    c.close()
    os._exit(0)


#1. 创建套接字 绑定 监听
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

#2. 收到客户端连接请求，创建新的进程
while True:
    try:
        c, addr = sockfd.accept()
    except KeyboardInterrupt:
        sockfd.close()
        os._exit(0)
    except Exception:
        continue
    print("connect seccess...",c.getpeername())
    
    pid = os.fork()
    if pid < 0:
        print("Create Process fail...")
        continue
    elif pid == 0:
        sockfd.close()
        print("处理客户端请求")
        handler(c)
    else:
        c.close()
        continue


#3. 主进程继续接收下一个客户端连接请求，子进程处理客户端事件
#4. 有客户端断开则关闭相应的子进程

