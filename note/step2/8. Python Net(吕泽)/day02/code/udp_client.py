from socket import *
import sys

#从命令行传入服务器的ＩＰ和端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#消息收发
while True:
    data = input("消息>>")
    #输入空客户端退出
    if not data:
        break
    #此处发送消息给服务器
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print("从服务器接收:",data.decode())

#关闭套接字
sockfd.close()