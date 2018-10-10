from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^show_request/$', show_request_views),
    url(r'^show_get/$', show_get_views),
    url(r'^login/', login_views,name='login'),
    url(r'^register/$',register_views),

]
