from socket import *

host = '127.0.0.1'
port = 8888
addr = (host, port)
buffersize = 1024

connfd = socket(AF_INET,SOCK_STREAM)

connfd.connect(addr)

while True:
    data = input("发送>>")
    if data == 'quit':
        break
    connfd.send(data.encode())
    data = connfd.recv(buffersize)
    print("接收>>", data.decode())

connfd.close()
