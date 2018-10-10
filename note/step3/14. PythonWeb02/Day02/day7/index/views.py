from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def show_request_views(request):
    # print(dir(request))
    scheme = request.scheme
    body = request.body
    path = request.path
    method = request.method
    host = request.get_host()
    get = request.GET
    post = request.POST
    cookie = request.COOKIES
    meta = request.META
    return render(request, 'show_request.html', locals())


def show_get_views(request):
    # 获取get请求提交的数据
    get = request.GET
    # name = request.GET['name']
    # age = request.GET['age']

    if 'name' in request.GET:
        name = request.GET['name']
    if 'age' in request.GET:
        age = request.GET['age']
    return render(request, 'show_get.html', locals())


def login_views(request):
    # 判断是post请求还是get请求,来分析用户的意图
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return HttpResponse('处理数据!')


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        if 'uname' in request.POST:
            uname = request.POST['uname']
        if 'upwd' in request.POST:
            upwd = request.POST['upwd']
        if 'uemail' in request.POST:
            uemail = request.POST['uemail']
        Users.objects.create(uname=uname, upass=upwd, uemail=uemail)
        return HttpResponse("Regist Success!")


# 1.创建数据库 usersdb
# 2.创建模型 users
#     uname, upass, uemail
#   映射到数据库中
# 3.提供一个 register.html
#     一个文本框,一个密码框,一个Email框,一个提交按钮
# 4.点击提交按钮时,提交给 /login/ 处理注册信息
#     获取文本框,密码框,Email框的值,并插入到数据库中
# 5.输入 http://localhost:8000/login 显示注册页面
