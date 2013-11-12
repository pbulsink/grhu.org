# sitemaps.py
from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

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

    def location(self, item):
        return reverse(item)

