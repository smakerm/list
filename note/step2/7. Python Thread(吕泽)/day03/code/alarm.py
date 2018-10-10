import signal 
import time 

#3秒后向自己发送一个SIGALRM信号
signal.alarm(3)

signal.alarm(8)

signal.pause()

while  True:
    time.sleep(1)
    print("等待时钟....")
