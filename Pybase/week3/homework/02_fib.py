
class Fibonacci:
    def __init__(self, n):
        self.__count = n

    def __iter__(self):
        return FiboIterator(self.__count)

class FiboIterator:
    def __init__(self, n):
        self.__count = n
        self.cur_count = 0
        self.a = 0
        self.b = 1
    def __next__(self):
        if self.cur_count >= self.__count:
            raise StopIteration
        self.cur_count += 1
        self.a ,self.b = self.b, self.a + self.b
        return self.a
        

for x in Fibonacci(10):
    print(x)

L = [x for x in Fibonacci(30)]
print(sum(Fibonacci(25)))
