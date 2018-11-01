from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^parent/$', parent_views),
    url(r'^child/$',child_views),
]
urlpatterns += [
    url(r'^add_author/$', add_author_views),
    url(r'^add_book/$',add_book_views),
    url(r'^add_publisher',add_publisher_views),
]

urlpatterns += [
    url(r'^get_authors/$',get_author_views),
]

urlpatterns += [
    url(r'^all_authors/$',all_authors_views),
]

urlpatterns += [
    url(r'^oto/$',oto_views),
    url(r'^otm/$',otm_views),
    url(r'^mtm/$',mtm_views),
]