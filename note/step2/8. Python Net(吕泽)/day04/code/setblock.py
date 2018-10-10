from socket  import *
import time

HOST = '172.60.50.218'
PORT = 8888 
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(5)

#将sockfd 变为非阻塞
# sockfd.setblocking(False)

#设置sockfd 的超时时间
sockfd.settimeout(5)


while True:
    print("wait for connect......")
    # time.sleep(8)
    #套接字等待客户端请求
    try:
        conn,addr = sockfd.accept()
        print("connect from ",addr)
        # conn.setblocking(False)
        while True:
            data = conn.recv(BUFFERSIZE)
            if not data:
                break
            print("接受到：",data.decode())
            n = conn.send(b"Recv your message\n")
            print("发送了　%d 字节的数据"%n)
        conn.close() 
    except Exception as e:
        print(e) 
    
sockfd.close() 