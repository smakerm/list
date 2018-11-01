from django.shortcuts import render
from django.http import HttpResponse,
from .models import *

# Create your views here.
def show_request_views(request):
    print(dir(request))
    return HttpResponse("Request Successful")

def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html',locals())
    else:
        if 'uname' in request.POST:
            uname = request.POST['uname']
        if 'upwd' in request.POST:
            upass = request.POST['upwd']

        obj = Users.objects.get(upass=upass,uname=uname)
        return render(request, 'index.html', locals())

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        if 'uname' in request.POST:
            uname = request.POST['uname']
        if 'upwd' in request.POST:
            upwd = request.POST['upwd']
        if 'uemail' in request.POST:
            uemail = request.POST['uemail']

        Users.objects.create(uname=uname, upass=upwd, uemail=uemail)
        return HttpResponse("regist Success!")