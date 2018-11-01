from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_views(request):
    return HttpResponse("Here is login page")
