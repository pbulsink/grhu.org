from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from about import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^agents/$', views.list, {'staff_type': 'Agent'}, name='about-agents'),
    url(r'^directors/$', views.list, {'staff_type': 'Director'}, name='about-directors'),
    url(r'^board/$', views.list, {'staff_type': 'Board'}, name='about-board'),
    url(r'^staff/$', views.list, name='about-list'),
    url(r'^staff/(?P<staff_id>[d]+)/$', views.staff),
    url(r'^vision/?$', RedirectView.as_view(url=reverse_lazy('vision')), name='about-vision'),
    url(r'^mission/?$', RedirectView.as_view(url=reverse_lazy('project')), name='about-mission'),

)

