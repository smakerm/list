from socket import * 
import os 

#设置通信的套接字文件
address = './sockfile'

try:
    os.unlink(address)  #删除这个目录下的这个文件
except OSError:
    if os.path.exists(address): #判断文件是否删除成功
        raise

s = socket(AF_UNIX,SOCK_STREAM)
s.bind(address) #绑定本地套接字的文件
s.listen(5)

while True:
    conn,addr = s.accept()
    print("connect from",addr) #addr是空子串
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("receive:",data)
        conn.send(b"receive your message")
    conn.close()
s.close()

