import gevent 
import time 

#协程函数
def foo(a,b):
    print("Running in foo",a,b)
    gevent.sleep(3)  #模拟遇到ＩＯ阻塞的情况
    print('switch to foo again')

def bar():
    print("Running in bar")
    gevent.sleep(2)
    print("switch to bar again")

#注册为协程事件
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)

# gevnet.join(f)
# gevnet.join(b)
gevent.joinall([f,b])