import gevent
import time

def foo(a, b):
    print("Running in foo",a,b)
    gevent.sleep(3)
    print("switch to foo again")

def bar():
    print("Running in bar")
    gevent.sleep(2)
    print("switch to bar again")


f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)

#gevent.join(f)
#gevent.join(b)
gevent.joinall([f, b])

