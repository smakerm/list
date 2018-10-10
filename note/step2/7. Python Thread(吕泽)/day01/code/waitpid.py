import os,sys 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print('Child process...')
    sleep(2)
    sys.exit(2) #子进程退出
else:
    #waitpid非阻塞等待子进程的退出
    p,status = os.waitpid(-1,os.WNOHANG)
    print(p,status)
    print(os.WEXITSTATUS(status))
    print('Parent process..')
    while True:
        pass
