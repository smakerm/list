from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add_cookie1/$', add_cookie1_views),
    url(r'^get_cookie1/$', get_cookie1_views),
    url(r'^add_session/$', add_session_views),
    url(r'^get_session/$', get_session_views),
]

urlpatterns += [
    url(r'^login/$', login_views),
    url(r'^index/$', index_views),
    url(r'^log_out/$', log_out_views),
]
