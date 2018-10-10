


class A:
    def m(self):
        print("A.m")

class B:
    def m(self):
        print("B.m")
class C(A):
    def m(self):
        print("C.m")
class D(B, C):
    def m(self):
        print("D.m")


d = D()
for i in D.__mro__:
    print(i)
d.m()

## super()是按照 mro 来查询的
