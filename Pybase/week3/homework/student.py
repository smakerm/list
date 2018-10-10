class Student:
    count = 0
    L = []

    def __init__(self, n, a = 0, s = 0):
        self.name = n
        self.age = a
        self.score = s
        
        self.__class__.count += 1
        self.__class__.L.append(self)

    def __del__(self):
        Student.count -= 1

    def get_score(self):
        return self.score

    @classmethod
    def getTotalCount(cls):
        return cls.count
    

s1 = Student("xiaoli", 18, 80)
s1 = Student("xiang", 20, 90)
s1 = Student("xiaoming", 25, 100)


print("当前学生总数为：", Student.getTotalCount())

#print(Student.L.score)

avg = sum([x.score for x in Student.L]) / Student.count

print("平均成绩：",avg)
