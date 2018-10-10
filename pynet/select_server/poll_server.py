#   基于poll的IO多路复用
from socket import *
import select

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8888))
s.listen(5)

#以每个IO对象的fileno为键，IO对象为值

fdmap = {s.fileno():s}

#创建poll对象
p = select.poll()

#添加关注的IO
p.register(s)

while True:
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from", addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send(b'receive you message')

s.close
