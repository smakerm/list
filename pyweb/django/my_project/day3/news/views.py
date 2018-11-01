from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_views(request):
    resp = HttpResponse("这是news的首页")
    return resp

def first_views(request):
    return render(request,'first.html')

def second_views(request):
    return render(request,'second.html')

def show_views(request, num):
    return HttpResponse("传递进来的参数为:" + num);

def result_views(request, num1, num2):
    return HttpResponse(num1 + '+' + num2 \
            + '=' + str(int(num1) + int(num2)))

def login_views(request):
    return render(request,'homework-login.html')