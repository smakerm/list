
'''此示例示意自定义的类能够转成数据类型'''


class MyNumber:
    def __init__(self, v):
        self.data = v
    def __repr__(self):
        return "MyNumber(%d)" % self.data
    
    def __int__(self):
        return 1111

n1 = MyNumber(100)

print (type(n1))

n = int(n1)

print(type(n), n)
