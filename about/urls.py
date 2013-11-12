from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^agent/$', views.agent, name='agent'),
    url(r'^directors/$', views.directors),
    url(r'^directors/(?P<name>[-_A-Za-z]+)/$', views.one_director, name='director'),
    url(r'^vision/?$', views.vision, name='vision'),
    url(r'^mission/?$', views.mission, name='mission')

)

