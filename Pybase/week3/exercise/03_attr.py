
class Car:
    def __init__(self, c, b):
        self.color = c
        self.brand = b

    def get_car_attr(self, attr_name):
        return getattr(self, attr_name, None)


c1 = Car("黑色", "Benz")

v = c1.get_car_attr('color')

if v is None:
    print('没有颜色属性')
else:
    print('颜色是:', v)
