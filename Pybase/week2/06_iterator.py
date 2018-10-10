

#L = [2, 3, 5, 7]
#
#
#
#it = iter(L)
#
#while True:
#    try:
#        x = next(it)
#        print(x)
#    except StopIteration:
#        break

s = {'A', 'B', 'C', 'D'}

it = iter(s)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print('遍历结束')
        break
