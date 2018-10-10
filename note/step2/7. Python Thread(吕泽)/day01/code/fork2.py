import os 
import time
from test import * 

#创建新的进程
pid = os.fork()

if pid < 0:
    print('create process failed')
elif pid == 0:
    fun1()
else:
    fun2()
