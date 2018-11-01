from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

# def login_views(request):
#     if request.method == 'GET':
#         cookies =  request.COOKIES
#         if 'id' in cookies and 'uphone' in cookies:
#             return HttpResponse('welcome %s'%(cookies.get('uphone')))
#         return render(request, 'homework-login.html')
#     else:
#         uphone = request.POST.get('uphone','')
#         upass = request.POST.get('upwd','')
#         if uphone and upass:
#             users = Users.objects.filter(uphone=uphone,upass=upass)
#             if users:
#                 u = users[0]
#                 resp = HttpResponse("welcome")
#                 if 'isSaved' in request.POST:
#                     resp.set_cookie('id',u.id, 60*60*24*365)
#                     resp.set_cookie('uphone',u.uphone,60*60*24)
#                 return resp
#             else:
#                 errMsg = "手机号或密码错误"
#                 return render(request,'homework-login.html',locals())
#         else:
#             errMsg = "手机号或密码不能为空"
#             return render(request, 'homework-login.html', locals())

def login_views(request):
    if request.method == "POST":
        uphone = request.POST.get('uphone', '')
        upass = request.POST.get('upwd', '')
        uList = Users.objects.filter(uphone=uphone,upass=upass)
        if uList:
            resp = HttpResponseRedirect('/index/')
            request.session['uphone'] = uphone
            if 'isSaved' in request.POST:
                resp.set_cookie('uphone', uphone ,3600)
            return resp
        else:
            errMsg = '手机号或密码不正确'
            return render(request,'homework-login.html',locals())
    else:
        if 'uphone' in request.session:
            return HttpResponseRedirect('/index/')
        else:
            if 'uphone' in request.COOKIES:
                uphone = request.COOKIES['uphone']
                resp = HttpResponseRedirect('/index/')
                request.session['uphone'] = uphone
                return resp
            else:
                print('123')
                return render(request,'homework-login.html')



def register_views(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        if 'uphone' in request.POST:
            uphone = request.POST['uphone']
        if 'upwd' in request.POST:
            upass = request.POST['upwd']
        if 'uemail' in request.POST:
            uemail = request.POST['uemail']
        if 'uname' in request.POST:
            uname = request.POST['uname']
        if upass and uname and uphone and uemail:
            u = Users.objects.filter(uphone=uphone)
            if u:
                errMsg = '手机号已存在'
                return render(request,'register.html',locals())
            else:
                Users.objects.create(uphone=uphone,upass=upass,uemail=uemail,uname=uname)
                return HttpResponseRedirect('/login')
        else:
            return render(request,'register.html',locals())

def index_views(request):
    return render(request, 'index.html')
    # if 'uphone' in request.COOKIES:
    #     return render(request,'index.html')
    # else:
    #     return HttpResponseRedirect('/login/')