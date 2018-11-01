from django.http import HttpResponse

def fun_views(request):
    return HttpResponse("Hello Django")

def index_views(request):
    return HttpResponse("index html")

def fun_arg1_views(request, num):
    return HttpResponse("传递的参数值为:" + num)


def fun_arg2_views(request, year, day, hour):
    resp = ("输入的时间为%s年%s月%s日%s时"%(year, day[:2], day[2:], hour))
    return HttpResponse(resp)

def fun_arg3_views(request, num):
    return HttpResponse("传递的参数值为:" + num)
