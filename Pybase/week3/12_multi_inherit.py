

class Car:
    def run(self, speed):
        print()


class Plane:
    def fly(self, height):
        print()

class PlaneCar(Car, Plane):
    pass


p1 = PlaneCar()

p1.fly()
p1.run()

## 多继承的缺陷：namespace 的冲突问题

##  广度优先
