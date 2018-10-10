

## 定义装饰器
def mydeco(fn):
    def fx():
        print('++++++++++++')
        fn()
        print('------------')
    return fx

## 定义函数
@mydeco
def myfunc():
    print("myfunc 被调用")



##  调用函数
myfunc()

