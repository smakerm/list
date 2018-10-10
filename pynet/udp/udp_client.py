from socket import *
import sys,time

BUFFERSIZE = 1024
ADDR = (sys.argv[1], int(sys.argv[2]))

#1. 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#2. 消息收发
while True:
    data = input("发送>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    data, addr = sockfd.recvfrom(BUFFERSIZE)
    print("从服务器接收：",data.decode())

#3. 关闭套接字
sockfd.close()

