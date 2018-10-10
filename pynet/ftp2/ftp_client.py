from socket import *
import sys
import time

class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b"L")

        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            pass
        else:
            print("get file list failed")
            return
        while True:
            data = self.sockfd.recv(1024).decode()
            if data == "##":
                break
            print(data)
        print("----done-------")
        return


    def do_get(self, filename):
        self.sockfd.send(b"G " + filename.encode())

        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            fd = open(filename, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
        else:
            print("download failed")
            return
    
    def do_put(self, filename):
        try:
            fd = open(filename, 'rb')
        except Exception:
            print("file not found")
            return
        self.sockfd.send(b"P " + filename.encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'ok':
            for line in fd:
                self.sockfd.send(line)
            fd.close()
            time.sleep(0.1)
            self.sockfd.send(b"##")
            print("upload %s done" %filename)
            return
        else:
            print("upload failed")
            retuen
    
    def do_quit(self):
        self.sockfd.send(b"Q")



def main():
    if len(sys.argv) != 3:
        print("argv is error")
        sys.exit(0)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.connect(ADDR)
    
    ftp = FtpClient(sockfd)
    while True:
        data = input(">> ")
        if data == 'list':
            ftp.do_list()
        elif data[:3] == 'get':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[:3] == 'put':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)
        elif data[:4] == 'quit':
            ftp.do_quit()
            sockfd.close()
            sys.exit(0)
        else:
            print("input error")
            continue

if __name__ == "__main__":
    main()
