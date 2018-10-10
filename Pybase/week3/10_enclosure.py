class A:
    def __init__(self):
        self.__p1 = 100  #__p 为私有属性，类外部无法访问

    def __m1(self):
        ''' __m1为私有方法，类外部无法使用，A类的子类也无法调用'''
        print("我是A类的__m1方法！")


a = A()
print(a.__p1) #无法调用
