from django.conf.urls import patterns, url

from photo_album import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='photo_album-index'),
)

