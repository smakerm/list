# 创建二级子进场解决僵尸进程
import os 

#创建一级子进程
pid = os.fork()

if pid < 0:
    print('create process failed')
elif pid == 0:
    #创建二级子进程
    p = os.fork()
    if p < 0:
        print('process failed')
    elif p == 0:
        print("做二级子进程任务")
    else:
        #一级子进程退出,使二级子进程成为孤儿
        os._exit(0)
else:
    #等待一级子进程退出
    os.wait()
    print("做父进程该做的")
