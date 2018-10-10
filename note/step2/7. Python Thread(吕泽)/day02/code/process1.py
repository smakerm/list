import multiprocessing as mp 
import os
import time 

#将要做的事封装为函数
def th1():
    print(os.getppid(),"----",os.getpid())
    print('吃饭早饭')
    time.sleep(1)
    print('吃饭午饭')
    time.sleep(2)
    print('吃饭晚饭')
    time.sleep(3)

def th2():
    print(os.getppid(),"----",os.getpid())
    print("睡午觉")
    time.sleep(1)
    print("睡觉")
    time.sleep(3)

def th3():
    print(os.getppid(),"----",os.getpid())
    print("打豆豆")
    time.sleep(2)
    print("打豆豆")
    time.sleep(2)

#创建3个子进程,生成子进程对象
#将函数和进程进行关联
p1 = mp.Process(target = th1)
p2 = mp.Process(target = th2)
p3 = mp.Process(target = th3)

#启动进程让其执行对应的函数事件
#该函数即为这个就进程内容
p1.start()
p2.start()
p3.start()

print("Parent PID:",os.getpid())

# 阻塞等对应子进程的退出,然后回收子进程
p1.join()
p2.join()
p3.join()

print("***********************")
# th1()
# th2()
# th3()
