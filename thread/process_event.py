from multiprocessing import Process,Event
import time

def wait_event():
    print("wait for event setting")
    e.wait()
    print("wait for event", e.is_set())

def wait_event_timeout():
    print("wait for event setting timeout")
    e.wait(2)
    print("wait for event", e.is_set())
    
e = Event()

p1 = Process(name = 'block',target = wait_event)
p2 = Process(name = 'non-block',target = wait_event_timeout)

p1.start()
p2.start()

print("主进程操作临界区")
time.sleep(3)
e.set()
print("主进程开放临界区")
