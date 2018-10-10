#基于select的ＩＯ多路复用监听服务器
from socket import * 
import select   #io多路服用模块
import sys

#s套接字作为一个ＩＯ事件
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('172.60.50.218',9999))
s.listen(5)

rlist = [s]
wlist = []
xlist = [s]

while True:
    #监听三个关注的列表中的ＩＯ事件
    rs,ws,es = select.select(rlist,wlist,xlist)
    print("哥等了一个世纪，有ＩＯ事件发生了")
    #通过for循环遍历每个返回列表，去处理ＩＯ
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            #将新的ＩＯ事件加入到监控列表
            rlist.append(c) 
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
            print("收到客户端消息：",data) 

    for w in ws:
        w.send("收到了你的消息".encode())
        wlist.remove(w)

    for e in es:
        if e is s:
            s.close()
            sys.exit(0)
        else:
            rlist.remove(e)
            xlist.remove(e)
            e.close()
