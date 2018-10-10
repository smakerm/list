from socket import *
import os


address = './sockfile'


try:
    os.unlink(address)

except OSError:
    if os.path.exists(address):
        raise

s = socket(AF_UNIX, SOCK_STREAM)
s.bind(address) #绑定本地套接字文件
s.listen(5)

while True:
    conn, addr = s.accept()
    print("connect from", addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("receive:", data)
        conn.send(b"receive your message")
    conn.close()

s.close()


