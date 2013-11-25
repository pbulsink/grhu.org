from django.conf.urls import patterns, url

from press import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='press-index'),
    url(r'^(?P<press_id>\d+)/$', views.detail, name='press-detail'),
    url(r'^list/$', views.list, name='press-list-1'),
    url(r'^list/(?P<list_pg>\d+)/$', views.list, name='press-lister')
)

