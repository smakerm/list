"""day2_exer URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
# from index import views as index_views
# from news import views as news_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #访问路径如果以index开始的话,则交给index应用的urls.py去处理
    url(r'^index/',include('index.urls')),

    # url(r'^index/login/$', index_views.login_views),
    # url(r'^news/login/$', news_views.login_views),
]
