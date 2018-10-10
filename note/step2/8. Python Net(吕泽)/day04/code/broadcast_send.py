from socket import *
from time import sleep

#设置发送的广播地址　，　<broadcast>
dest = ('172.60.50.255',9999) 

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("喜迎两会，习大大带你飞".encode(),dest)
    data,addr = s.recvfrom(1024)
    print(data.decode())

s.close()