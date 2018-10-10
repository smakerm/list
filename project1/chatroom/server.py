from socket import *
import sys
import os
import signal
import time

def do_login(s, user, name, addr):
    for i in user:
        if i == name or name == "管理员":
            s.sendto(b'Fail',addr)
            return
    s.sendto(b'ok',addr)
    msg = "欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr
    log = "%s:%s -- [%s]  %s"%(*addr,time.ctime(),name)
    print(log)
    return

def do_chat(s, user, tmp ):
    msg = "%-4s : %s"%(tmp[1],' '.join(tmp[2:]))
    for i in user:
        if i != tmp[1]:
            s.sendto(msg.encode(),user[i])
    return

def do_qiut(s, user, name):
    del user[name]
    msg = name + '离开了聊天室'
    for i in user:
        s.sendto(msg.encode(),user[i])
    return
    

#接收消息
def do_child(s):
    user = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msg = msg.decode()
        tmp = msg.split(' ')
        if tmp[0] == 'L':
            do_login(s, user, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, user, tmp)
        elif tmp[0] == 'Q':
            do_qiut(s, user, tmp[1])

#发送消息
def do_parent(s, addr):
    name = "C 管理员 "
    while True:
        msg = input("管理员消息:")
        msg = name + msg
        s.sendto(msg.encode(), addr)
    s.close()
    sys.close()


def main():
    if len(sys.argv) != 3:
        print("argv error")
        sys.exit(0)
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    pid = os.fork()
    if pid < 0:
        print("create process falid")
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s, ADDR)

if __name__ == "__main__":
    main()
