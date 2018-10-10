

class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.money = 0
    
    def teach(self, other, skill):
        print(self.name, '教', other, '学',skill)

    def works(self, money):
        self.money += money
        print(self.name, '工作赚了', money, '元钱')

    def borrow(self, other, money):
        if other.money > money:
            self.money += money
            other.money -= money
        else:
            print(other.name)

zhang3 = Human('张三', 35)
li4 = Human('李四',10)

zhang3.teach('李四','python')
li4.teach
