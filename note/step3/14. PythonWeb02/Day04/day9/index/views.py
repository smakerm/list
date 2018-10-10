from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def add_cookie1_views(request):
    # 创建响应对象
    resp = HttpResponse("请求成功,将数据保存进cookie")
    # 通过响应对象,添加cookie进客户端
    resp.set_cookie('uname', 'zhangsanfeng@163.com', 60 * 60 * 24 * 2)
    return resp


def get_cookie1_views(request):
    # print(request.COOKIES)
    # 获取 COOKIES 中,键为 uname 的值
    if 'uname' in request.COOKIES:
        return HttpResponse(request.COOKIES['uname'])
    return HttpResponse('获取cookies成功')


def add_session_views(request):
    # 向session中存储用户名称
    request.session['uname'] = 'John Lennon'
    # 设置为关闭浏览器,session则失效
    request.session.set_expiry(0)
    return HttpResponse("Add Session OK")


def get_session_views(request):
    # 获取 session 的键为 uname 的值
    if 'uname' in request.session:
        uname = request.session.get('uname')
        return HttpResponse('欢迎:' + uname)
    return HttpResponse('对不起,未取到数据')


def login_views(request):
    if request.method == 'GET':
        uname = request.session.get('uname', '')
        return render(request, 'login.html', locals())
    else:
        uname = request.POST.get('uname', '')
        upwd = request.POST.get('upwd', '')
        if uname and upwd:
            if uname == 'zhangsanfeng' and upwd == 'yinsusu':
                request.session['uname'] = uname
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("用户名或密码错误")
        else:
            return HttpResponse("用户名或密码不能为空")


def index_views(request):
    if 'uname' in request.session:
        uname = request.session.get('uname')
        return HttpResponse('欢迎' + uname + '来到首页!!')
    else:
        return HttpResponse('欢迎!!!')


def log_out_views(request):
    del request.session['uname']
    return HttpResponseRedirect('/index/')
