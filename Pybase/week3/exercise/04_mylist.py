
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        return MyList(self.data * lhs)

    def __iadd__(self, rhs):
        self.data.extend(rhs.data)
        return self
    


L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)

L4 = L2 + L1
print (L4)

L5 = L1 * 2
print(L5)

L6 = 2 * L1  #出错，反向算术运算符的重载
print(L6)
