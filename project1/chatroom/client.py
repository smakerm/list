from socket import *
import sys
import os
import signal

#发送消息
def do_child(s, addr, name):
    while True:
        text = input('发言：')
        if text == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            os.kill(os.getppid(),signal.SIGKILL)
            sys.exit(0)
        else:
            msg = "C %s %s"%(name, text)
            s.sendto(msg.encode(), addr)

#接收
def do_parent(s):
    while True:
        msg, addr = s.recvfrom(1024)
        print('\n' + msg.decode() + '\n发言：',end='')


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

    while True:
        name = input("请输入姓名：")
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'ok':
            print("欢迎进入聊天室")
            break
        else:
            print("用户名已存在，请重新输入")

    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    pid = os.fork()
    if pid < 0:
        print("create process falid")
    elif pid == 0:
        do_child(s, addr, name)
    else:
        do_parent(s)


if __name__ == "__main__":
    main()
