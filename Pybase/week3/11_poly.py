##


class Shape:
    def draw(self):
        print("Shap.draw")


class Point(shape):
    def draw(self):
        print("正在画点")

calss Circle(Point):
    def draw(self):
        pritn("正在画圈")

def my_draw(s):
    s.draw()   #  此处显示多态中的动态

s1 = Circle()
s1 = Point()

my_draw(s1)
