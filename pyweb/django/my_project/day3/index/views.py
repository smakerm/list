from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_views(request):
    resp = HttpResponse('<h1>这是首页</h1>')
    return resp

def login_views(request):
    resp = HttpResponse('<h1>这是登陆页面</h1>')
    return resp