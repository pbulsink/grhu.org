from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Content',  {'fields': ['title', 'byline', 'content', 'description']}),
        ('Author Info', {'fields': ['author', 'author_email']})
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publish Time',  {'fields': ['pub_date', 'mod_date', 'public']}),
    ]

admin.site.register(News, NewsAdmin)

