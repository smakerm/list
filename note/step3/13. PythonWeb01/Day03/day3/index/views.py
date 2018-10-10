from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#配置首页的视图
def index_views(request):
    resp = HttpResponse('<h1>这是首页</h1>')
    return resp

#配置login_views视图
def login_views(request):
    resp = HttpResponse('<h1>这是登录页面</h1>')
    return resp
