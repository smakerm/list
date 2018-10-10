from greenlet import greenlet 


#协程函数
def test1():
    print(111111111)
    gr2.switch()
    print(222222222)
    gr2.switch()

def test2():
    print(333333333)
    gr1.switch()
    print(444444444)

#讲函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
