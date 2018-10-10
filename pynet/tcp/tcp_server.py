from socket import *

host = '127.0.0.1'
port = 8888
addr = (host, port)
buffersize = 1024

#1. 创建一个tcp流式套接字
sockfd = socket(AF_INET, SOCK_STREAM)

#   设置端口号可以立即重用
sockfd.setsocketopt(SOL_SOCKET, SO_REUSEADDR, 1)

#2. 绑定本机IP和端口号
sockfd.bind(addr)

#3. 将套接字变为可监听的套接字
sockfd.listen(3)
while True:
    #4. 套接字等待客户端的请求
    print("wait for connect......")
    conn, addr = sockfd.accept()
    print("connect from", addr)
    while True:
        #5.  消息的收发
        msg = conn.recv(buffersize)
        if not msg:
            break
        print("收到了：", msg.decode())
        #data = "hello"
        n = conn.send(b"Recv your message")
        print("收到了 %d 字节的数据"%n)

    #6. 关闭套接字
    conn.close()    #断开连接

sockfd.close()  #关闭客户端
