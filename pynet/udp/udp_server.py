from socket import *
import sys,time

BUFFERSIZE = 1024
ADDR = (sys.argv[1], int(sys.argv[2]))

#1. 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地IP和端口
sockfd.bind(ADDR)

#3. 收发消息
while True:
    print("wait to recv......")
    data, addr = sockfd.recvfrom(BUFFERSIZE)
    if not data:
        break
    print("recv from", addr, ':',data.decode())
    sockfd.sendto(("在 %s 接收到你的消息"%time.ctime()).encode(), addr)
#4. 关闭套接字

sockfd.close()
