import os


pid = os.fork()


if pid < 0:
    print("Error")

elif pid > 0:
    print()
    cid = os.fork()
    if pid < 0:
        print("Error")
    else if = 0:
        print("做二级子进程工作")
    else:
        #一级子进程退出，使二级子进程成为孤儿进程
        os._exit(0)

else:
    os.wait()
    print()
