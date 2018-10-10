from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index_views(request):
    resp = HttpResponse('这是news的首页')
    return resp


def first_views(request):
    return render(request, 'first.html')


def second_views(request):
    return render(request, 'second.html')


def show_views(request, num):
    return HttpResponse("传递进来的参数为:" + num)


def result_views(request, num1, num2):
    r = int(num1) + int(num2)
    return HttpResponse(r)


def var_views(request):
    l = ['张三丰', '张无忌', '张翠山']
    t = ('赵敏', '殷素素', '周芷若')
    d = {'a': 'ABC', 'b': 'BEYOND'}
    dic = {
        'num': 125,
        'str': 'Hello Django',
        'list': l,
        'tup': t,
        'dic': d,
        'fun': fun(25, 52),
        'A': A(),
    }
    return render(request, 'var.html',dic)


def fun(a, b):
    return a + b


class A(object):
    def f(self):
        return "A -> f()"
