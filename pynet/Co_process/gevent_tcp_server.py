import gevent
#monkey 脚本插件的使用要在导入socket之前
#他改变了socket模块的阻塞状态
from gevent import monkey
monkey.patch_all()
from socket import *

def handler(c, addr):
    print("Connect from", addr)
    while True:
        data = c.recv(1024).decode()
        if data == '':
            break
        print("receive ", data)
        c.send(b"Receive your message")
    c.close()

HOST = '127.0.0.1'
PORT = 8889
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(20)

while True:
    c, addr = s.accept()
    gevent.spawn(handler, c, addr)

s.close()
