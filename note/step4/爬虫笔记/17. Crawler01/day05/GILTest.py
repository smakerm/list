import threading

def f():
    # 死循环
    while True:
        pass

if __name__ == '__main__':
    t=threading.Thread(target=f)
    t.start()

    while True:
        pass
