
class MyNumber:
    def __init__(self, v):
        self.data = v

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    def __add__(self, other):
        v = self.data + other.data
        return MyNumber(v)

    def __sub__(self, other):
        v = self.data - other.data
        return MyNumber(v)


n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2

print(n3)

n4 = n3 - n1

print(n4)
