from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog Content',  {'fields': ['title', 'byline', 'content', 'description']}),
        ('Author Info', {'fields': ['author', 'author_email']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publish Time',  {'fields': ['pub_date', 'mod_date', 'public']}),
    ]


admin.site.register(Blog, BlogAdmin)

