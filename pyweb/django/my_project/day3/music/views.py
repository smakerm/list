from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index_views(request):
    resp = HttpResponse("<h1>这是music的首页</h1>")
    return resp

def music_show_views(request):
    t = loader.get_template("show.html")
    html = t.render({'title':'Django模板'})
    return HttpResponse(html)

def music_info(request):
    # t = loader.get_template('music_info.html')
    dict = {
        'mName' : '小苹果',
        'author': '筷子兄弟',
        'player': '筷子兄弟',
    }
    # html = t.render(dict)
    # return HttpResponse(html)
    return render(request,'music_info.html',dict)