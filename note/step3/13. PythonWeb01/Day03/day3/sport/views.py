from django.shortcuts import render

# Create your views here.


def person_views(request):
    uname = "sanfeng.zhang"
    uage = 58
    ugender = 1
    uhobby = ['打太极', '撩妹', '聊骚']
    return render(request, 'person.html', locals())
