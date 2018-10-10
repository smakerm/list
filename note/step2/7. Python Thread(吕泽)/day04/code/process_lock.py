from multiprocessing import Process,Lock
import time,sys 

def worker1(stream):
    lock.acquire() # 加锁
    for i in range(5):
        time.sleep(1)
        stream.write("Lock acquired via\n")
    lock.release()#解锁

def worker2(stream):
    # lock.acquire()
    with lock:    #加锁　语句块结束即解锁
        for i in range(5):
            time.sleep(1)
            stream.write("Lock acquired directly\n")
    # lock.release()

lock = Lock()
#sys.stdout为所有进程都拥有的资源
w1 = Process(target=worker1,args=(sys.stdout,))
w2 = Process(target=worker2,args=(sys.stdout,))

w1.start()
w2.start()

w1.join()
w2.join()