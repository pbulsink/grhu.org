from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog Content',  {'fields': ['title', 'content']}),
        ('Image Content', {'fields': ['image', 'tooltip']}),
        ('Publish Time',  {'fields': ['pub_date']}),
    ]


admin.site.register(Blog, BlogAdmin)

