import time
import os


def fun1():
    print("执行函数1")
    time.sleep(3)

def fun2():
    print("执行函数2")
    time.sleep(2)


pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print(os.getppid())
    time.sleep(3)
    print(os.getppid())
    print("This is new process")
else:
    print("This is the parent process")

print("This process end")
