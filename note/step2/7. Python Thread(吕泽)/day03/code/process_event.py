from  multiprocessing import Process,Event
import time 

def wait_event():
    print('process1要等主进程操作完我才能操作')
    e.wait()
    print('终于操作完了，该我了',e.is_set())

def wait_event_timeout():
    print('process2要等主进程操作完我才能操作')
    e.wait(2)
    print('我等不了了，干别的去',e.is_set())

e = Event() 

p1 = Process(name = 'block',\
    target = wait_event)
p1.start()
p2 = Process(name = 'non-block',\
    target = wait_event_timeout)
p2.start()

print("假设主进程在忙碌的操作临界区")
time.sleep(3)
e.set()
print("主进程开放临界区")
