from threading import Thread

import queue
import time

#创建一个队列
q = queue.Queue()
count = 0

class Producer(Thread):
	def run(self):
		global count
		while True:
			if q.qsize() < 50:
				for i in range(3):
					count += 1
					msg = "产品 %d"%count
					q.put(msg)
					print("生产了一个 --------->%s"%msg)
			time.sleep(1)
			


class Customer(Thread):
	def run(self):
		while True:
			if q.qsize() > 20:
				for i in range(2):
					msg = q.get()
					print("消费了一个%s"%msg)
					
					
for i in range(3):
	p = Producer()
	p.start()
	
for i in range(5):
	p = Customer()
	p.start()
