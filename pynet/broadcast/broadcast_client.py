from socket import *
from time import sleep

dest = ('<broadcast>', 8888)

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


while True:
    s.sendto("broadcast mail".encode(), dest)
    data, addr = s.recvfrom(1024)
    print(data.decode())
    sleep(2)


s.close()
