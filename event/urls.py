from django.conf.urls import patterns, url

from event import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^upcoming/?$', views.upcoming, name='upcoming'),
    url(r'^past/?$', views.past, name='past'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
)

