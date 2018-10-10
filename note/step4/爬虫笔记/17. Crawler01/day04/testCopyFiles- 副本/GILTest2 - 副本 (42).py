import multiprocessing

def f():
    # 死循环
    while True:
        pass

if __name__ == '__main__':
    t=multiprocessing.Process(target=f)
    t.start()

    while True:
        pass
