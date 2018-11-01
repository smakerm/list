from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index_views),
    url(r'^show/$',music_show_views),
    url(r'^music_info/$',music_info),
]
