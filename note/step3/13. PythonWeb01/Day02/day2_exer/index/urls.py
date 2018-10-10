from django.conf.urls import url
from .views import *

#此处为 index 应用的路由配置文件
urlpatterns = [
    url(r'^login/$',login_views),
]