from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog Content',  {'fields': ['title', 'byline', 'content']}),
        ('Author Info', {'fields': ['author', 'author_email']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publish Info',  {'fields': ['pub_date', 'public', 'description'],
            'classes': ['collapse']}),
    ]


admin.site.register(Blog, BlogAdmin)

