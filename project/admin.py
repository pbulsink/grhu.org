from django.contrib import admin
from project.models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['pub_date']}),
        ('Project',     {'fields': ['title', 'content', 'active']}),
        ('Title Image', {'fields': ['image', 'tooltip']}),
    ]

admin.site.register(Project)

