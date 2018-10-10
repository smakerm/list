from multiprocessing import Process,Lock
import time,sys

def worker1(stream):
#    lock.acquire()
    with lock:
        for i in range(5):
            time.sleep(1)
            print("worker1")
#    lock.release()
        
def worker2(steam):
#    lock.acquire()
    with lock:
        for i in range(5):
            time.sleep(1)
            print("worker2")
#    lock.release()

lock = Lock()


w1 = Process(target=worker1, args=(sys.stdout,))
w2 = Process(target=worker2, args=(sys.stdout,))

w1.start()
w2.start()

w1.join()
w2.join()
    
        
