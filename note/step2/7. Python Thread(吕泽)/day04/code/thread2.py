import threading
from time import sleep,ctime 

def fun():
    print("This is a thread test")
    sleep(5)
    print("thread over")

t = threading.Thread(name = 'levi',\
    target = fun)

# t.setDaemon(True)
t.daemon = True 
print(t.isDaemon())

t.start()

print(t.is_alive())  #线程状态
print(t.name) #线程名称

t.join(2)

print("all over",ctime())


