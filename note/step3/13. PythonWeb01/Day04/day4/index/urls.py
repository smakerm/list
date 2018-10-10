from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^parent/$', parent_views),
    url(r'^child/$', child_views),
]
