from django.contrib import admin
from news.models import News, Comments

class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 5

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('News Content',  {'fields': ['title', 'content']}),
        ('Image Content', {'fields': ['image', 'tooltip']}),
        ('Publish Time',  {'fields': ['pub_date']}),
    ]
    inlines = [CommentsInline]

admin.site.register(News, NewsAdmin)

