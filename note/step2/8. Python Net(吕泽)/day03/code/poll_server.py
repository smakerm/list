#基于ｐｏｌｌ的ＩＯ多路复用
from socket import *
import select 

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('172.60.50.218',9999))
s.listen(5)

#以每个ＩＯ对象的fileno为键，io对象为值
fdmap = {s.fileno():s}

#创建ｐｏｌｌ对象
p = select.poll()
#添加关注的ＩＯ
p.register(s)

while True:
    #监控关注的ＩＯ
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from ",addr)
            #将客户端套接字添加关注并添加到字典
            p.register(c)
            fdmap[c.fileno()] = c  
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024).decode()
            #如果客户端退出则不在关注，并且从字典移除
            if not data:
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data)
                fdmap[fd].send('收到你的消息'.encode())
s.close()