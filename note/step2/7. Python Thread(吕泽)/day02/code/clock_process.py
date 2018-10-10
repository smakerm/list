from multiprocessing import Process
import time 

class ClockProcess(Process):
    def __init__(self,value):
        Process.__init__(self) 
        self.value = value 

    # 在process类中实现的,现在重写这个函数

    def run(self):
        n = 5
        while n > 0:
            print('The time is {}'.\
                format(time.ctime()))
            time.sleep(self.value)
            n -= 1

#s使用自己的进程类创建进程对象
p = ClockProcess(2)
#start后会自动执行run函数
p.start()
p.join()
