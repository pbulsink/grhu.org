from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Content',  {'fields': ['title', 'byline', 'content', 'description']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publish Time',  {'fields': ['pub_date', 'mod_date', 'public', 'active']}),
    ]

admin.site.register(Project, ProjectAdmin)

