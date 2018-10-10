"""day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 如过访问路径为 fun/ 的话,
    # 则交给fun_views视图处理函数去处理
    url(r'^fun/$', fun_views),

    # 模拟首页的地址匹配
    url(r'^$', index_views),

    # 匹配 fun/\d{2,}
    url(r'^fun/(\d{2,})', fun_arg1_views),

    #练习
    url(r'^(\d{2})/(\d{4})/(\d{2})',get_url1_views),
    url(r'^(\w{2,3})/(\d{4})',get_url2_views),

    url(r'^shownames/$',show_views,{'name':'zsf','age':'25'})
]
