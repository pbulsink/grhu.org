from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^agents/$', views.agent, name='about-agents'),
    url(r'^directors/$', views.directors, name='about-directors'),
    url(r'^directors/(?P<name>[-_A-Za-z]+)/$', views.one_director),
    url(r'^staff/$', views.list, name='about-list'),
    url(r'^staff/(?P<staff_id>[d]+)/$', views.staff, name='about-staff'),
    url(r'^vision/?$', views.vision, name='grhu-vision'),
    url(r'^mission/?$', views.mission, name='grhu-mission'),

)

