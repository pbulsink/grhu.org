from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Content',  {'fields': ['title', 'content']}),
        ('Image Content', {'fields': ['image', 'tooltip']}),
        ('Publish Time',  {'fields': ['pub_date']}),
    ]

admin.site.register(News, NewsAdmin)

