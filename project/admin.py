from django.contrib import admin
from project.models import Project, Images

class ImageInline(admin.StackedInline):
    model = Images
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['pub_date']}),
        ('Project',     {'fields': ['title', 'content', 'active']}),
        ('Title Image', {'fields': ['image', 'tooltip']}),
    ]
    inlines = [ImageInline]

admin.site.register(Project)

