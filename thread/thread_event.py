from threading import *
import random
from time import sleep

a = 500

e = Event()

def fun():
	global a 
	while True:
		sleep(0.5)
		print("消耗货物：a =", a)
		e.wait()
		a -= random.randint(0,100)


t = Thread(target = fun)
t.start()
while True:
	sleep(0.5)
	a += 10
	print("生产货物：a = ",a)
	if a > 100:
		e.set()
	else:
		e.clear()



t.join()
