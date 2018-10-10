class MyList:
    def __init__(self, iterator):
        self.data = list(iterator)

    def __repr__(self):
        return "MyIterable(%r)" % self.data
    
    def __iter__(self):
        print("__iter__被调用")
        return MyListIterator(self.data)


class MyListIterator:
    '''此类用来创建一个迭代器对象'''
    def __init__(self, iter_data):
        self.cur = 0  #设置迭代器的初始值为0
        self.it_data = iter_data
    def __next__(self):
        '''有此方法的对象才是迭代器
        此方法一定要实现迭代器协议'''
        if self.cur >= len(self.it_data):
            raise StopIteration

        r = self.it_data[self.cur]
        self.cur += 1
        return r

myl = MyList([2, 3, 5, 7])

print(myl)

for i in myl:
    print(i)
