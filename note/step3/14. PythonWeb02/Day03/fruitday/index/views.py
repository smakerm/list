from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def login_views(request):
    # 判断request.method是get还是post
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uphone = request.POST.get('uphone', '')
        upwd = request.POST.get('upwd', '')
        # if uphone and upwd:
        #     users = Users.objects.filter(uphone=uphone, upass=upwd)
        #     if users:
        #         return HttpResponse('登录成功!!')
        #     else:
        #         errMsg = '手机号或密码不正确'
        #         return render(request, 'login.html', locals())
        if uphone and upwd:
            users = Users.objects.filter(uphone=uphone)
            if users:
                u = users[0]
                if upwd == u.upass:
                    return HttpResponse('登录成功')
                else:
                    errMsg = '对不起,输入的密码不正确'
                    return render(request, 'login.html', locals())
            else:
                errMsg = '对不起,手机号码不存在'
                return render(request, 'login.html', locals())
        else:
            errMsg = '手机号或密码不能为空'
            return render(request, 'login.html', locals())


def register_views(request):
    # 判断request.method 得到用户的意图
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 实现注册操作
        uphone = request.POST.get('uphone', '')
        upwd = request.POST.get('upwd', '')
        uname = request.POST.get('uname', '')
        uemail = request.POST.get('uemail', '')

        if uphone and upwd and uname and uemail:
            # 先判断uphone的数据是否存在
            u = Users.objects.filter(uphone=uphone)
            if u:
                errMsg = '手机号码已存在'
                return render(request, 'register.html', locals())
            else:
                Users.objects.create(uphone=uphone, upass=upwd,
                                     uname=uname, uemail=uemail)
                return HttpResponse('注册成功!!!')
        else:
            return HttpResponse('数据不能为空')
