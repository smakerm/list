import os 

pid = os.fork()

if pid < 0:
    print('create process failed')
elif pid == 0:
    print("Child process:")
    print("当前进程的PID:",os.getpid())
    print("当前进程父进程的PID:",os.getppid())
else:
    print("Parent process:")
    print("pid:",pid)
    print("当前进程的PID号:",os.getpid())