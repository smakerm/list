from greenlet import greenlet

def test1():
    print(1111111111)
    gr2.switch()
    print(2222222222)
    gr2.switch()

def test2():
    print(3333333333)
    gr1.switch()
    print(4444444444)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
