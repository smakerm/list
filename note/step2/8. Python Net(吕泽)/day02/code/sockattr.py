from socket  import *
import time

HOST = '172.60.50.218'
PORT = 8888 
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

sockfd = socket(AF_INET,SOCK_STREAM)

print("您的套接字是：",sockfd.type)
print("sockfd 的　file num:",sockfd.fileno())

#将端口号设置为立即重用
sockfd.setsockopt\
(SOL_SOCKET,SO_REUSEADDR,1)

print("获取选项值：",sockfd.\
    getsockopt(SOL_SOCKET,SO_REUSEADDR))

sockfd.bind(ADDR)

sockfd.listen(5)

print("您的套接字地址是：",sockfd.getsockname())

while True:
    print("wait for connect......")
    conn,addr = sockfd.accept()
    #使用getpeername获取链接的客户端的地址
    print("connect from ",conn.getpeername())

    while True:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print("接受到：",data.decode())
        n = conn.send(b"Recv your message\n")
        print("发送了　%d 字节的数据"%n)
  
    conn.close()    # 表示和客户端断开连接
    
sockfd.close() # 不能再使用sockfd