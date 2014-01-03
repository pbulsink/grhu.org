# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime

from about.models import About
from blog.models import Blog
from event.models import Event
from news.models import News
from press.models import Press
from project.models import Project
#from photo_album.models import Album

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['index',
                'terms',
                'privacy',
                'sitemap',
                'vision',
                'contact',
                'helpout',
                'donate',
                ]

    def lastmod(self):
        return datetime.date(2014,01,03)

    def location(self, item):
        return reverse(item)

class AboutSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return About.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.pub_date


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Blog.objects.filter(public=True)

    def lastmod(self, obj):
        return obj.mod_date


class EventSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Event.objects.filter(public=False)

    def lastmod(self, obj):
        return obj.pub_date


class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return News.objects.filter(public=False)

    def lastmod(self, obj):
        return obj.mod_date


class PressSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Press.objects.filter(public=False)

    def lastmod(self, obj):
        return obj.mod_date


class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Project.objects.filter(public=False)

    def lastmod(self, obj):
        return obj.pub_date
