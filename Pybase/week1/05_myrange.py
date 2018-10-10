def myrange(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
    L = []
    i = start
    if step > 0:
        while i < stop:
            L.append(i)
            i += step
        return L
    else:
        while i > stop:
            L.append(i)
            i += step
        return L


def myrange2(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
        print(1)
    L = []
    i = start
    while i < stop:
        L.append(i)
        i += step
    return L


print(myrange(1,3))

print(myrange(10,0,-1))
