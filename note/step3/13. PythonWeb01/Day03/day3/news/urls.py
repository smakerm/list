from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views),
    url(r'^first/$', first_views),
    url(r'^second_pages/$', second_views,name='my'),
    url(r'^show/(\d+)/$',show_views,name='show'),
    url(r'^result/(\d+)/(\d+)',result_views,name='cal'),
]

urlpatterns += [
    url(r'^variable/$',var_views),
]
