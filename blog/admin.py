from django.contrib import admin
from blog.models import Blog, Comments

class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 5

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Blog Content',  {'fields': ['title', 'content']}),
        ('Image Content', {'fields': ['image', 'tooltip']}),
        ('Publish Time',  {'fields': ['pub_date']}),
    ]
    inlines = [CommentsInline]

admin.site.register(Blog, BlogAdmin)

