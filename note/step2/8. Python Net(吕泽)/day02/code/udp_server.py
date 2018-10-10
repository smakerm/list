from socket import * 
import sys 
from time import ctime

#从命令行传入ＩＰ和端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFFERSIZE = 5

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定本地IP和端口
sockfd.bind(ADDR)

#收发消息
while True:
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print("recv from ",addr,':',data.decode())
    sockfd.sendto\
    (("在　%s 接受到你的消息"%ctime()).encode(),addr)

#关闭套接字
sockfd.close()