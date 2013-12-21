from django.conf.urls import patterns, url

from photo_album import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='album-index'),
    url(r'^latest/$', views.latest, name='album-latest'),
)

