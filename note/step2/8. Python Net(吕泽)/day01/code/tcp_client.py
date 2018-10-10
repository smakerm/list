from socket import *
import time

#要链接的服务器的地址信息
HOST = '172.60.50.218'
PORT = 8888 
ADDR = (HOST,PORT)

#创建客户端套接字要和访问的服务器的套接字类型相同

connfd = socket(AF_INET,SOCK_STREAM)

#链接服务器
connfd.connect(ADDR)

while True:
    data = input("发送>>")
    if not data:
        break 
    #和服务器进行通信
    connfd.sendall(data.encode())

    data = connfd.recv(1024)
    print("客户端收到：",data.decode())

# time.sleep(2)

#关闭套接字
connfd.close() #和服务器断开链接