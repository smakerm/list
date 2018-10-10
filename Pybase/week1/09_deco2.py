
def messend(fn):
    def fx(name, x):
        print("send ")
        fn(name, x)
        print("send", name, '办了', x)
    return fx


def savemoney(name, x):
    print(name, "存钱", x , '元')

@messend
def withdraw(name, x):
    print(name, "取钱", x , '元')


savemoney('xx', 200)

withdraw('xx',300)

