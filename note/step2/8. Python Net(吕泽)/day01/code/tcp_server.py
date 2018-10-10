#python网络套接字模块
from socket  import *

HOST = '172.60.50.218'
PORT = 8888 
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#创建一个tcp流式套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定本机的IP和端口号
sockfd.bind(ADDR)

#将套接字变为可监听套接字 
sockfd.listen(5)

while True:
    print("wait for connect......")
    #套接字等待客户端请求
    conn,addr = sockfd.accept()
    print("connect from ",addr)
    # 消息的收发
    while True:
        data = conn.recv(BUFFERSIZE)
        if not data:
            break
        print("接受到：",data.decode())
        n = conn.send(b"Recv your message\n")
        print("发送了　%d 字节的数据"%n)
    #关闭套接字
    conn.close()    # 表示和客户端断开连接
    
sockfd.close() # 不能再使用sockfd