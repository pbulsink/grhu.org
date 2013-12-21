from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='blog-index'),
    url(r'^(?P<blog_id>\d+)/$', views.detail, name='blog-detail'),
    url(r'^list/$', views.list, name='blog-list-1'),
    url(r'^list/(?P<list_pg>\d+)/$', views.list, name='blog-lister'),
    url(r'^latest/$', views.latest, name='blog-latest'),
)
