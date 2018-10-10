from socket import *
import os 
import signal  

#有客户端断开则关闭相应的子进程
def handler(c):
    while True:
        data = c.recv(BUFFERSIZE).decode()
        if not data:
            break
        print("服务器收到：",data)
        c.send(b'receive your message')
    c.close()
    os._exit(0)

#创建套接字  绑定  监听
HOST = '172.60.50.218'
PORT = 8888
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#创建tcp套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
s.bind(ADDR)
s.listen(5)

#做僵尸进程的处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

#接收客户端连接请求  创建新的进程
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        print("服务器结束")
        s.close()
        os._exit(0)
    except Exception:
        continue
    print("接收到客户端链接　＞",c.getpeername())

    pid = os.fork()
   
    if pid < 0:
        print("创建子进程失败")
        continue
    #子进程处理客户端事件
    elif pid == 0:
        s.close()
        print('处理客户端请求事件')
        handler(c) # 处理客户端的函数
    #主进程继续接收下一个客户端连接请求
    else:
        c.close()
        continue

