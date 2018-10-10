import threading
from time import ctime,sleep

def music(sec):
    print(sec)
    sleep(sec)
    print("Listening music")

    
t = threading.Thread(name="my thread", target=music, args=(3,))

#t.setDaemon(True)
#t.daemon = True
t.start()

print(t.isDaemon())

t.join(2)

print("创建线程")
