import threading 
from time import ctime,sleep 

a = 10

def music(sec):
    print("Listening music")
    global a
    a = 1000
    sleep(sec)

t = threading.Thread(name = "my thread",\
    target = music,args = (2,))

t.start()
print("创建线程")
sleep(3)
print(a)
