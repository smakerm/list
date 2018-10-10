from threading import * 
import random 
from time import sleep 

a = 500

#创建事件对象
e = Event()

#子线程不断减少a 但是希望a的值不会少于100
def fun():
    global a
    while True:
        sleep(2)
        print('a = ',a)
        e.wait()
        a -= random.randint(0,100)

t = Thread(target = fun)
t.start()

#主线程不断的让a增加以确保a不会小于100
while True:
    sleep(1)
    a += random.randint(1,10)
    if a > 100:
        e.set()
    else:
        e.clear()

t.join()