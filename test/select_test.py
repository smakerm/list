# 基于select 的IO多路复用监听服务器

from socket import *
import select

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    #监听三个列表中的IO事件
    rs, ws, es = select.select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from", addr)
            rlist.append(c) #将新的IO事件加入到监控列表
            xlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                print("客户端退出")
                rlist.remove(r)
                xlist.remove(r)
                r.close()
            else:
                wlist.append(r)
#            print("收到客户端消息：",data)


    for w in ws:
        k.send('h'.encode())
        wlist.remove(w)
    for e in es:
        if e is s:
            s.close()
            sys.exit(0)
        else:
            e.close()
            rlist.remove(e)
            xlist.remove(e)
s.close()
