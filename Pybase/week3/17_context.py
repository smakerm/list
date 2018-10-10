class A:
    def __enter__(self):
        print("已进入with语句")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''此方法会在退出with语句时自动调用
        exc_type 在没有异常时为None，在出现异常时绑定异常类型
        exc_val                     ,                错误对象
        exc_tb                       ,               traceback '''
        print("以离开with语句")

with A() as a:
    print("这是with语句内的一条语句")


## with 语句  与 环境管理器
