from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<news_id>\d+)/$', views.detail, name='detail'),
    url(r'^/list/$', views.list, name='list1'),
    url(r'^/list/(?P<list_pg>\d+)/$', views.list, name='lister')
)

