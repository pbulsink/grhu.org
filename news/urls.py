from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='news-index'),
    url(r'^(?P<news_id>\d+)/$', views.detail, name='news-detail'),
    url(r'^list/$', views.list, name='news-list-1'),
    url(r'^list/(?P<list_pg>\d+)/$', views.list, name='news-lister')
)

