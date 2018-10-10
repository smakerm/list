from django.shortcuts import render

# Create your views here.


def parent_views(request):
    return render(request, 'parent.html')


def child_views(request):
    return render(request, 'child.html')
