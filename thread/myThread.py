from time import ctime,sleep
import threading


class MyThread(threading.Thread):
	def __init__(self, func, args, name="levi"):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
		self.name = name
		
	def run(self):
		self.func(*self.args)
	
		
def player(file, time):
	for i in range(2):
		print("start playing %s:%s"%(file,ctime()))
		sleep(time)
		
t = MyThread(player,('boby.mp3',3))

t.start()

t.join()
