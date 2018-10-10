from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


# def login_views(request):
#     # 判断request.method是get还是post
#     if request.method == 'GET':
#         # 判断 id 和 uphone 是否都存在与 COOKIES 中
#         cookies = request.COOKIES
#         if 'id' in cookies and 'uphone' in cookies:
#             return HttpResponse('欢迎:' + cookies['uphone'])
#         return render(request, 'login.html')
#     else:
#         uphone = request.POST.get('uphone', '')
#         upwd = request.POST.get('upwd', '')
#         # if uphone and upwd:
#         #     users = Users.objects.filter(uphone=uphone, upass=upwd)
#         #     if users:
#         #         return HttpResponse('登录成功!!')
#         #     else:
#         #         errMsg = '手机号或密码不正确'
#         #         return render(request, 'login.html', locals())
#         if uphone and upwd:
#             users = Users.objects.filter(uphone=uphone)
#             if users:
#                 u = users[0]
#                 if upwd == u.upass:
#                     resp = HttpResponse('登录成功')
#                     # 判断是否要记住密码
#                     if 'isSave' in request.POST:
#                         # 将用户id,uname保存进cookie
#                         resp.set_cookie('id', u.id, 60 * 60 * 24 * 365)
#                         resp.set_cookie('uphone', u.uphone, 60 * 60 * 24 * 365)
#                         return resp
#                     else:
#                         return HttpResponse('登录成功')
#                 else:
#                     errMsg = '对不起,输入的密码不正确'
#                     return render(request, 'login.html', locals())
#             else:
#                 errMsg = '对不起,手机号码不存在'
#                 return render(request, 'login.html', locals())
#         else:
#             errMsg = '手机号或密码不能为空'
#             return render(request, 'login.html', locals())

def login_views(request):
    if request.method == 'POST':
        # 执行登录的验证判断
        uphone = request.POST.get('uphone', '')
        upwd = request.POST.get('upwd', '')
        uList = Users.objects.filter(uphone=uphone, upass=upwd)
        if uList:
            # 登录成功
            # 声明一个响应对象
            resp = HttpResponseRedirect('/index/')
            # 将手机号码存进session
            request.session['uphone'] = uphone
            # 判断是否需要存进cookie
            if 'isSave' in request.POST:
                resp.set_cookie('uphone', uphone, 3600 * 24 * 365)
            return resp
        else:
            # 登录失败
            errMsg = '手机号或密码不正确'
            return render(request, 'login.html', locals())
    else:
        # GET请求
        # 判断是否处于已登录状态(session中是否有值)
        if 'uphone' in request.session:
            return HttpResponseRedirect('/index/')
        else:
            # 未处于登录状态
            # 判断曾经是否登录过(cookies中是否有值)
            if 'uphone' in request.COOKIES:
                # 曾经登陆过,取出值,存进session
                uphone = request.COOKIES['uphone']
                request.session['uphone'] = uphone
                return HttpResponseRedirect('/index/')
            else:
                # 不曾登陆过
                return render(request, 'login.html')


def index_views(request):
    return render(request, 'index.html')


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
