from django.http import HttpResponse

# 视图,处理用户的请求并给出响应
# request:表示用户的请求信息
# HttpResponse:响应给客户端的内容


def fun_views(request):
    return HttpResponse('Hello Django')


def index_views(request):
    return HttpResponse('这是网站的首页')

# 处理 url(r'^fun/(\d{2,})',fun_arg1_views)的请求的
# num表示的是第一个参数(第一个子组)的值


def fun_arg1_views(request, num):
    resp = HttpResponse('传递的参数值为:' + num)
    return resp

# 练习的处理
# url(r'^(\d{2})/(\d{4})/(\d{2})',get_url1_views),


def get_url1_views(request, year, day, hour):
    resp = HttpResponse(year + ":" + day + ":" + hour)
    return resp

# url(r'^(\w{2,3})/(\d{4})',get_url2_views),


def get_url2_views(request, country, day):
    resp = HttpResponse(country + ":" + day)
    return resp

def show_views(request,name,age):
    resp = HttpResponse(name+":"+age)
    return resp