from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\[-0-9a-zA-Z)/?', views.details, name='project'),
    url(r'^shoes/?$', views.shoes, name='shoes'),
)

