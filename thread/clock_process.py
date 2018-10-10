from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self, value):
        Process.__init__(self)
        self.value = value

    def run(self):
        n = 5
        while n > 0:
            print("This time is {}".format(time.ctime()))
            time.sleep(self.value)
            n -= 1

p = ClockProcess(2)
p.start()
p.join()
