from math import sqrt

## isprime(x)  判断是否为素数
def isprime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


## prime_m2n(m,n) m到n(不包含n)的素数
def prime_m2n(m, n):
    L = []
    for i in range(m, n):
        if isprime(i):
            L.append(i)
    return L


## primes(n) 返回指定范围内的素数
def primes(n):
    L = prime_m2n(2, n)
    print(L)
    print(sum(L))

primes(100)
