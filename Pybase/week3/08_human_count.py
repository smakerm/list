
#  用类变量记录对象个数


class Car:
    count = 0
    def __init__(self, info):
        pritn(info , '被创建')
        self.data = info
        self.__class__.count += 1

    def __del__(self):
        print(self.date, '被销毁')
        self.__class__.count -= 1



