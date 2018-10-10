from socket import *
from threading import Thread

class socketInfoModule(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind((self.ip,self.port))
        self.clientAddr = ''
    def sendInfo(self):
        while True:
            if not self.cllientAddr:
                self.s.sendto(b'receive your message',  self.clientAddr)

    def recvInfo(self):
        while True:
            data, addr = self.s.recvfrom(1024).decode()
            if data == '##':
                self.clientAddr = ''
                break
            self.clientAddr = addr
            print("recv message:", data)


        
