class Student:
    def __init__(self, name, age = 0, score = 0):
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        print(self.name, '今年', self.age,'岁' )

    def set_score(self, s):
        self.score = s


s1 = Student('校长', 20)
s2 = Student('小李', 18)
s1.show_info()
s2.show_info()
