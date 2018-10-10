from multiprocessing import Process,Pipe 
import os,time

#创建管道对象
#当参数为False的时候child只能recv parent只能send
# child_conn,parent_conn = Pipe(False)

child_conn,parent_conn = Pipe()

#子进程函数
def fun(name):
    time.sleep(1)
    #发送一个字符串到管道
    child_conn.send('hello' + str(name))
    print(os.getppid(),"----",os.getpid())

jobs = []
#创建５个子进程
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = parent_conn.recv()
    print(data)

for i in jobs:
    i.join()