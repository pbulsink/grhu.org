from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='project-index'),
    url(r'^(?P<project_id>\d+)/$', views.detail, name='project-detail'),
    url(r'^list/$', views.list, name='project-list-1'),
    url(r'^list/(?P<list_pg>\d+)/$', views.list, name='project-lister'),
    url(r'^latest/$', views.latest, name='project-latest'),
    url(r'^(?P<url>.*)/$', views.project_finder),
   
)

