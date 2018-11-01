from django.conf.urls import url
from .views import *

urlpatterns = [
    # url('^$',index_views),
    url('^first/$',first_views),
    url('^second_pages/$',second_views,name='my'),
    url(r'^show/(\d+)$',show_views,name='show'),
    url(r'^result/(\d)/(\d)/$',result_views,name='result'),
    url('^$',login_views),
]

