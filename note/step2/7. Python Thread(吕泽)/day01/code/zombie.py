import os 
import time

pid = os.fork()

if pid < 0:
    print("create new process failed")
elif pid == 0:
    print("父进程的PID",os.getppid())
    time.sleep(3)
    print("父进程的PID",os.getppid())
    print("子进程退出了")
    os._exit(0) 
else:
    # time.sleep(1)
    print('Child PID:',pid)
    # while True:
    #     pass