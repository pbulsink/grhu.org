from django.conf.urls import patterns, url

from event import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='event-index'),
    url(r'^upcoming/?$', views.upcoming, name='event-upcoming'),
    url(r'^recent/?$', views.recent, name='event-recent'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='event-detail'),
    url(r'^list/$', views.list, name='event-list-1'),
    url(r'^list/(?P<list_pg>\d+)/$', views.list, name='event-lister'),
    url(r'^latest/$', views.latest, name='event-latest'),
)

