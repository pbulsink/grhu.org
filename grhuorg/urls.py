from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from sitemaps import StaticViewSitemap, AboutSitemap, BlogSitemap, EventSitemap
from sitemaps import NewsSitemap, PressSitemap, ProjectSitemap, FrontPagesSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'about': AboutSitemap,
    'blog': BlogSitemap,
    'event': EventSitemap,
    'news': NewsSitemap,
    'press': PressSitemap,
    'project': ProjectSitemap,
    'front': FrontPagesSitemap,
}

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grhuorg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^projects/', include('project.urls')),
    url(r'^press/', include('press.urls')),
    url(r'^events/', include('event.urls')),
    url(r'^albums/', include('photo_album.urls')),
    url(r'^$', 'grhuorg.views.index', name='index'),
    url(r'^home/?$', 'grhuorg.views.home', name='home'),
    url(r'^terms/?$', 'grhuorg.views.terms', name='terms'),
    url(r'^privacy/?$', 'grhuorg.views.privacy', name='privacy'),
    url(r'^donate/?$', 'grhuorg.views.donate', name='donate'),
    url(r'^contact/?$', 'grhuorg.views.contact', name='contact'),
    url(r'^contact-us/?$', 'grhuorg.views.contact', name='contact'),
    url(r'^vision/?$', 'grhuorg.views.vision', name='vision'),
    url(r'^sitemap/?$', 'grhuorg.views.sitemap', name='sitemap'),
    url(r'^mission/?$', 'grhuorg.views.mission', name='mission'),
    url(r'^helpout/?$', 'grhuorg.views.helpout', name='helpout'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})

    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

