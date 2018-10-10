import threading 
from time import sleep 

s = None 

e = threading.Event()

def bar():
    print("呼叫foo")
    global s 
    s = "天王盖地虎"

def foo():
    print('foo等口令')
    sleep(2)
    print('foo收到　%s'%s)
    e.set()

def fun():
    sleep(1)
    e.wait()
    print("内奸出现")
    global s 
    s = "小鸡炖蘑菇"   

t1 = threading.Thread\
(name = 'bar',target = bar)

t2 = threading.Thread\
(name = 'foo',target = foo)

t3 = threading.Thread\
(name = 'fun',target = fun)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
