
class Car:
    def __init__(self, c, b, m):
#        print('')
        self.color = c
        self.brand = b
        self.model = m

        def run(self, speed):
            print(self.color, self.brand, self.model, '正在以', speed)

a2 = Car('红色', '奥迪', 'A4')
