from multiprocessing import Pool 
import time 

def fun(fn):
    time.sleep(1)
    return fn * fn 

test = [1,2,3,4,5,6]

print("顺序执行:")
s = time.time()
for i in test:
    fun(i)
e = time.time()
print('执行时间:',e - s)

print("进程池执行")
pool = Pool(processes = 4)

r = pool.map(fun,test)
pool.close()
pool.join()
print('执行时间:',time.time() - e)


