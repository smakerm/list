from socket import * 
from time import sleep

address = './sockfile'

s = socket(AF_UNIX,SOCK_STREAM)

try:
    s.connect(address)
except error as e:
    print(e)

try:
    message = b"This is a unix message"
    s.send(message)
    # sleep(20)
    data = s.recv(1024).decode()
    print('recv:',data)
except error as e:
    print(e)
finally:
    s.close()