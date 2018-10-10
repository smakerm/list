from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def remark_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, 'remark.html', locals())
    else:
        # 接收提交的数据
        # 1.将POST中的数据放在RemarkForm中
        form = RemarkForm(request.POST)
        # 2.判断当前数据是否通过验证(必须的)
        if form.is_valid():
            # 3.获取提交的数据并封装到cd中
            cd = form.cleaned_data
            # 4.获取每个控件的值
            print(cd['subject'])
            print(cd['mail'])
            print(cd['message'])
            print(cd['topic'])
            return HttpResponse('Query OK')
        else:
            return HttpResponse('Error')


def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Users(**cd).save()
        return HttpResponse("Register Success!")


def model_form_views(request):
    if request.method == 'GET':
        form = UsersForm()
        return render(request, 'model_form.html', locals())
    else:
        form = UsersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Users(**cd).save()
            return HttpResponse('Register OK')


def login_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', locals())


def widget1_views(request):
    form = WidgetForm()
    return render(request, 'widget.html', locals())
