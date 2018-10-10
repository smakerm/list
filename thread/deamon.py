import multipeocess as mp
from time import sleep

def fun()
    print('Child process start')
    sleep(3)
    print('Child process end')

p = mp.Process(target = fun)
p.start()
p.join()


print("********main process end************")
