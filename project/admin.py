from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Content',  {'fields': ['title', 'byline', 'content']}),
        ('Project Timing', {'fields': ['start_date', 'end_date', 'active']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publishing',  {
            'fields': ['pub_date', 'public', 'description', 'short_query'],
            'classes': ['collapse']}),
    ]

admin.site.register(Project, ProjectAdmin)

