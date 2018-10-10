import gevent
#monkey 脚本插件的使用要在导入socket之前
#它改变了socket模块的阻塞部分
from gevent import monkey 
monkey.patch_all()
from socket import * 

#协程事件
def handler(c,addr):
    print("Connect from",addr)
    while True:
        data = c.recv(1024).decode()
        if not data:
            break 
        print("Recv msg:",data)
        c.send(b"Receive your message")
    c.close()

HOST = '172.60.50.218'
PORT = 9999
ADDR = (HOST,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(20)

while True:
    c,addr = s.accept()
    gevent.spawn(handler,c,addr)

s.close()

