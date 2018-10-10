from threading import Thread 
#python标准库中的队列模块
import queue 
import time  

#创建一个队列模型作为商品的仓库
q = queue.Queue()

class Producer(Thread):
    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(3):
                    count += 1
                    msg = "产品　%d"%count
                    q.put(msg)  #将产品放入队列
            time.sleep(1)

class Customer(Thread):
    def run(self):
        while True:
            if q.qsize() > 20:
                for i in range(2):
                    msg = q.get() #从仓库拿到商品
                    print("消费了一个　%s"%msg)
            time.sleep(1)

#创建三个生产者
for i in range(3):
    p = Producer()
    p.start()

#创建５个消费者
for i in range(5):
    p = Customer()
    p.start()