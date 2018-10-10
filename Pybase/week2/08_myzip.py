 def myzip(iter1, iter2):
    '''zip函数的实现机制'''
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        x = next(it1)
        y = next(it2)
        yield (x, y)

 
 
 numbers = [10086, 10000, 10010, 95588]
 names = ['中国移动', '中国电信', '中国联通']


 for x in zip(numbers, names):
    print(x)

##  ()
##  ()
##  ()

