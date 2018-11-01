from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def remark_views(request):
    if request.method == 'GET':
        form = RemarkFrom()
        return render(request, 'remark.html', locals())

    else:
        form = RemarkFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
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
        return render(request,'register.html',locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Users(**cd).save()
            return HttpResponse('Register success')

def model_form_views(request):
    if request.method == 'GET':
        form = UsersForm()
        return render(request,'model_form.html',locals())