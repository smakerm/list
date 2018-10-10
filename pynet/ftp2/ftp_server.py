from socket import *
import os
import sys
import signal
import time

FILE_PATH = '/root/bin/pycharm2017/lib/'

class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd
    
    def do_list(self):
        filelist = os.listdir(FILE_PATH)
        if not filelist or filelist == None:
            self.connfd.send(b"Fail")
        self.connfd.send(b"ok")
        time.sleep(0.1)
        for f in filelist:
            
            if f[0] != '.' and os.path.isfile(FILE_PATH + f):
                self.connfd.send(f.encode() + b'\n')
        time.sleep(0.1)
        self.connfd.send(b"##")
        print("filelist send done")
        return

    def do_get(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'rb')
        except:
            self.connfd.send(b'Failed')
        self.connfd.send(b'ok')
        time.sleep(0.1)
        for line in fd:
            self.connfd.send(line)
        fd.close()
        time.sleep(0.1)
        self.connfd.send(b'##')
        print("send file done")
        return


    def do_put(self, filename):
        try:
            fd = open(FILE_PATH + filename, 'wb')
        except:
            self.connfd.send(b"failed")
        self.connfd.send(b"ok")
        time.sleep(0.1)
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print("upload done")
        return




def main():
    if len(sys.argv) != 3:
        print("argv is erros")
        sys.exit(1)
        
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            print("wait connect...")
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue
        print("Connect from %s at %s" %(addr, time.ctime()))
        pid = os.fork()
        if pid < 0:
            print("Create child process filed")
            continue
        elif pid == 0:
            sockfd.close()
            ftp = FtpServer(connfd)
            while True:
                data = connfd.recv(BUFFERSIZE).decode()
                if data[0] == 'L':
                    ftp.do_list()
                elif data[0] == 'G':
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)
                elif data[0] == 'P':
                    filename = data.split(' ')[-1]
                    ftp.do_put(filename)
                elif data[0] == 'Q':
                    print("client quit")
                    sys.exit(0)
        else:
            connfd.close()
            continue


if __name__ == "__main__":
    main()
