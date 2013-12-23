from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Content',  {'fields': ['title', 'byline', 'content']}),
        ('Author Info', {'fields': ['author', 'author_email']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publishing',  {'fields': ['pub_date', 'public', 'description'],
            'classes': ['collapse']}),
    ]

admin.site.register(News, NewsAdmin)

