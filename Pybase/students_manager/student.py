class Student:
    count = 0

    def __init__(self, n, a = 0, s = 0):
        self.name = n
        self.age = a
        self.score = s
        
        self.__class__.count += 1

    def __del__(self):
        Student.count -= 1

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_info(self):
        return (self.name, self.age, self.score)

    def is_exist(self, name):
        return self.name == name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
            return
        raise ValueError("input error")

    def write_to_file(self, f):
        f.write(self.name)
        f.write(',')
        f.write(str(self.age))
        f.write(',')
        f.write(str(self.score))
        f.write('\n')

    @classmethod
    def getTotalCount(cls):
        return cls.count
