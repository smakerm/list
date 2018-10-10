
#def myyield():
#    '''此函数为生成器函数
#    在生成器函数中调用return
#    会返回 StopIterator 对象'''
#    print("即将生成：")
#    yield 2
#    print("即将生成：")
#    yield 3
#    print("即将生成：")
#    yield 5
#
#gen = myyield()
#it = iter(gen)
#
#next(it)    # 输出  即将生成：2
#next(it)    # 输出  即将生成：2
#next(it)    # 输出  即将生成：2


##def myinteger(n):
##    '''生成器函数内的变量不消失'''
##    i = 0
##    while i < n:
##        yield i
##        i += 1
##    return
##
##
##for i in myinteger(3):
##    print(i)
##
##
##it = iter(myinteger(2))
##
##print(next(it))
##print(next(it))
##print(next(it))


#生成器表达式：
gen = (x**2 for x in range(1,4) )

#for i in gen:
#    print(i)

it = iter(gen)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
