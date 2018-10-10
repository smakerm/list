from socket import *

host = '127.0.0.1'
port = 8888
addr = (host, port)
buffersize = 1024

connfd = socket(AF_INET,SOCK_STREAM)

connfd.connect(addr)

while True:
    msg = input("发送>>")
    if not msg:
#        connfd.send(msg.encode())
        break
    connfd.send(msg.encode())
    data = connfd.recv(buffersize)
    print("客户端收到:", data.decode())

connfd.close()
