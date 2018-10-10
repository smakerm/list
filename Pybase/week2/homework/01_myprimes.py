import math


def is_primes(x):
    for i in range(2,math.ceil(math.sqrt(x))):
        if x % i == 0:
            return False
    return True
        

#  用生成器
def primes(start, end):
    '''生成 [start,end) 的全部素数'''
    for i in range(start, end):
        if is_primes(i):
            yield i

L = [x for x in primes(10,20)]

print(L)
