from multiprocessing import Process
from time import sleep

def work(sec, msg):
    for i in range(3):
        sleep(sec)
        print("the worker msg:",msg)

p = Process(name='wrokre',target=work,args=(2,),\
            kwargs={'msg':'You are big man'})

p.start()
p.join
